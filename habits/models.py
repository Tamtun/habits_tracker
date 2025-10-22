from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )
    period = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Время в секундах")
    is_public = models.BooleanField(default=False)

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError(
                "Нельзя одновременно указать вознаграждение и связанную привычку."
            )
        if self.duration > 120:
            raise ValidationError("Время выполнения не должно превышать 120 секунд.")
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")
        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError(
                "Приятная привычка не может иметь вознаграждение или связанную привычку."
            )
        if self.period < 1 or self.period > 7:
            raise ValidationError("Периодичность должна быть от 1 до 7 дней.")

    def __str__(self):
        return f"{self.action} в {self.time} в {self.place}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

