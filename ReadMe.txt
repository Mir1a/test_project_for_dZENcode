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

   git clone git@github.com:Mir1a/test_project_for_dZENcode.git
   cd test_project_for_dZENcode

2. Создайте виртуальное окружение и активируйте его:

    python -m venv .venv
    .venv\Scripts\activate

3. Создайте .env файл с вашими переменными среды:

Пример:

DB_HOST=db
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres


4. Установите зависимости:

    pip install -r requirements.txt


5. Примените миграции:

    python manage.py migrate

6. Запустите сервер разработки:

    python manage.py runserver

7. Доступ к приложению:

    Swagger UI: http://127.0.0.1:8000/swagger/

Установка с использованием docker:

1. Клонируйте репозиторий:

   git clone git@github.com:Mir1a/test_project_for_dZENcode.git
   cd test_project_for_dZENcode

2. Создайте .env файл с вашими переменными среды:

Пример:

DB_HOST=db
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres


3. Запустите docker-compose

    docker-compose up --build

4. Доступ к приложению:

    Swagger UI: http://127.0.0.1:8000/swagger/

    API Эндпоинты

    Без авторизации:

GET /user/ - Получить список всех пользователей.
POST /user/ - Создать нового пользователя.
POST /token/ - Получение JWT токена.
POST /token/refresh/ - Обновление access токена через refresh токен.

Защищенные эндпоинты (требуется авторизация):
Для доступа к этим эндпоинтам необходимо использовать Bearer токен.
Токен передается в заголовке авторизации:

Authorization: Bearer <токен>

GET /comments/ - Получить список всех комментариев.
POST /comments/ - Создать новый комментарий.
