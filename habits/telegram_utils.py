import requests
from django.conf import settings



def send_telegram_message(chat_id: str, text: str) -> bool:
    token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    return response.status_code == 200
