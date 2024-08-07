# Bike Rental Service

## Установка и запуск

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/TheLLiRRiKminD/bicycle_rental_backend
    cd bike_rental
    ```

2. Запустите Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. Создайте суперпользователя:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. Откройте браузер и перейдите по адресу `http://localhost:8000/swagger/` для просмотра документации API.