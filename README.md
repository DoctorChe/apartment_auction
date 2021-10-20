# apartment_auction
Веб-приложение «Аукцион квартир»

## Предварительные настройки
1. Необходимо настроить переменные окружения:
```shell
cp example.env .env
```
- `HOST_PORT` - порт хостовой машины, куда будет проброшен порт FastAPI из контейнера
- `POSTGRES_PASSWORD` - пароль для подключения к PostgreSQL.
- `CONSOLE_LOGGING_LEVEL` - уровень логирования.
- `POSTGRES_VOLUME` - путь для сохранения данных на хост машине.

Значения по умолчанию
- `POSTGRES_USER=postgres`  # default user
- `POSTGRES_HOST=db`  # to docker container
- `POSTGRES_PORT=5432`  # default postgres port
- `POSTGRES_DATABASE=postgres`  # default database

## PROD
Для запуска в production необходимо выполнить команду:
```shell
docker-compose -f docker-compose.yml up --build
```

## DEV
Для запуска в dev среде необходимо выполнить команду:
```shell
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```
По умолчанию FastAPI запускается в режиме без обновления исходного кода приложения в реальном времени.  
В `docker-compose.dev.yml` задаётся команда `/start-reload.sh` для запуска с обновления исходного кода приложения в реальном времени.  
См. https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#development-live-reload


## DB
База данных PostgreSQL.  

- Имя суперпользователя по умолчанию `postgres`
- Пароль задается в переменных окружения
- Порт по умолчанию 5432


## При развертывании новой базы
1. Для начальной инициализации данных необходимо выполнить команду
    ```shell
    docker-compose exec backend python backend/initial_data.py
    ```