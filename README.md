# Habit Tracker

Habit Tracker — это Django‑приложение для отслеживания привычек с поддержкой Celery, Redis и PostgreSQL.  
Проект упакован в Docker и готов к деплою через GitHub Actions.

---
## 📌 Адрес сервера с развёрнутым приложением:
89.169.173.157

## 📌 Локальный запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/Tamtun/habits_tracker.git
cd habits_tracker
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Установка зависимостей 
```bash
pip install -r requirements.txt
```

### 4. Настройка .env

Создайте файл .env в корне проекта, на основе .env.sample:

```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=habits_db
DB_USER=habits_user
DB_PASSWORD=supersecret
DB_HOST=localhost
DB_PORT=5432
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### 5. Применение миграций и запуск сервера

```bash
python manage.py migrate
python manage.py runserver
```
## 📌 Запуск через Docker Compose
```bash
docker compose up -d --build
```

## 📌 CI/CD и деплой на сервер

### 1. Подготовка сервера

Установите Docker и Docker Compose.

Склонируйте проект:

```bash
git clone https://github.com/Tamtun/habits_tracker.git ~/habit_tracker
cd ~/habit_tracker
```
Создайте .env с реальными значениями (не хранится в GitHub).

### 2. GitHub Actions Workflow
В репозитории есть .github/workflows/deploy.yml

### 3. Настройка секретов GitHub

В настройках репозитория → Settings → Secrets → Actions добавьте:

SERVER_IP — IP или домен сервера

SSH_USER — SSH‑пользователь (например, intes)

SSH_KEY — приватный ключ для доступа

### 4. Проверка деплоя
Сделайте коммит и пуш в develop.

GitHub Actions запустит workflow.

На сервере контейнеры перезапустятся автоматически.

