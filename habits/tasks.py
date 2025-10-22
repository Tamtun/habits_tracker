from celery import shared_task
from .models import Habit
from .telegram_utils import send_telegram_message
from datetime import datetime


@shared_task
def send_reminder(habit_id):
    try:
        habit = Habit.objects.get(id=habit_id)
        chat_id = "ЧАТ АЙДИ ПОЛЬЗОВАТЕЛЯ"  # ⬅️ Укажите чат айди пользователя
        message = f"Напоминание: {habit.action} в {habit.time} в {habit.place}"
        send_telegram_message(chat_id, message)
    except Habit.DoesNotExist:
        print(f"Habit {habit_id} не найдена.")
    except Exception as e:
        print(f"Ошибка при отправке напоминания: {e}")


@shared_task
def schedule_reminders():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_weekday = now.weekday()

    habits = Habit.objects.filter(time=current_time)

    for habit in habits:
        if habit.period and (current_weekday % habit.period != 0):
            continue

        send_reminder.delay(habit.id)
