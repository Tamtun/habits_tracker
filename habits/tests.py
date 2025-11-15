from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from habits.models import Habit, Profile
from datetime import time
from django.core.exceptions import ValidationError

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123')

    def test_create_valid_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place='дом',
            time=time(10, 0),
            action='читать',
            period=1,
            duration=60,
            is_pleasant=False
        )
        self.assertEqual(habit.action, 'читать')
        self.assertEqual(habit.user, self.user)

    def test_invalid_duration(self):
        habit = Habit(
            user=self.user,
            place='дом',
            time=time(10, 0),
            action='читать',
            period=1,
            duration=180,
            is_pleasant=False
        )
        with self.assertRaises(ValidationError):
            habit.clean()


class HabitAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_habit_api(self):
        response = self.client.post('/api/habits/', {
            "place": "дом",
            "time": "10:00",
            "action": "читать",
            "period": 1,
            "duration": 60,
            "is_pleasant": False
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['action'], 'читать')


class ProfileSignalTest(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username='newuser', password='123')
        profile = Profile.objects.get(user=user)
        self.assertIsNotNone(profile)

