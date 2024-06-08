# Приложение для создания видео с бегущей строкой

## Запуск
- установить вирутальное окружение: python -m venv env
- создать файл .env.dev, в котором указать:
    - DEBUG
    - SECRET_KEY
    - DJANGO_ALLOWED_HOSTS
    - SQL_ENGINE=django.db.backends.postgresql
    - SQL_DATABASE
    - SQL_USER
    - SQL_PASSWORD
    - SQL_HOST
    - SQL_PORT
    - DATABASE (postgres)
- запустить docker-compose.yml up -d --build
- переходим на localhost:8000/runtext?message=(Ваше сообщение)
