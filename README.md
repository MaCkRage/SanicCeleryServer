Microservice Empty Python
# Установка

```bash
git clone <GIT-РЕПОЗИТОРИЙ_ВАШЕГО_ПРОЕКТА>

cd <НАЗВАНИЕ_ВАШЕГО_ПРОЕКТА>
```

Переключаемся на ветку `staging`

```bash
git checkout staging

git push -u origin staging
```

Копируем файл `example.env` в файл `.env`

```bash
cp example.env .env
```

Редактируем файл `.env` и изменяем `SECRET_KEY` на любой набор символов, например, название сайта.
Все остальные параметры можно не трогать.

Устанавливаем виртуальное окружение

```bash
virtualenv python3.7 -m venv venv
```

Поднимаем базу данных с помощью докера

```bash
docker-compose up -d
```

Активируем виртуальное окружение

```bash
source venv/bin/activate
```

Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

# Запуск сервера

```bash
python manage.py run

```
# Запуск celery (из папки backend)
```bash
celery -A celery.celery worker -B -l INFO 
опционально:
...INFO --loglevel=DEBUG
```

# Запуск тестов (пока не работают)

```bash
python -m unittest
```

