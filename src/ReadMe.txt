# Проект API для Комментариев

Это проект на Django для управления комментариями и пользователями. Проект использует Django REST framework для создания API и `drf-yasg` для генерации документации в формате Swagger.

Возможности

- Создание и чтение комментариев.
- Поддержка вложенных комментариев.
- Управление пользователями и их комментариями.
- Документация API с использованием Swagger UI и Redoc.

Требования

Все необходимые зависимости указаны в файле `requirements.txt`. Установите их командой:

pip install -r requirements.txt

Установка

1. Клонируйте репозиторий:

   ```bash
   git clone
   cd src

2. Создайте виртуальное окружение и активируйте его:

    python -m venv .venv
    .venv\Scripts\activate

3. Установите зависимости:

    pip install -r requirements.txt

4. Примените миграции:

    python manage.py migrate

5. Запустите сервер разработки:

    python manage.py runserver

6. Доступ к приложению:

    Swagger UI: http://127.0.0.1:8000/swagger/


    API Эндпоинты:

GET /comments/ - Получить список всех комментариев.
POST /comments/ - Создать новый комментарий.
GET /user/ - Получить список всех пользователя.
POST /user/ - Создать нового пользователя.

POST /token/ - Получение jwt токена
POST /token/refresh/ - Обновление access токена через refresh токен