FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Установка системных зависимостей (для PostgreSQL и сборки пакетов)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Переменные окружения (можно переопределять через .env)
ENV SECRET_KEY="dev_secret"
ENV CELERY_BROKER_URL="redis://redis:6379/0"
ENV CELERY_BACKEND="redis://redis:6379/0"

# Создаём папку для медиа
RUN mkdir -p /app/media

# Открываем порт для Django
EXPOSE 8000

# По умолчанию запускаем Django (Celery будет запускаться через docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
