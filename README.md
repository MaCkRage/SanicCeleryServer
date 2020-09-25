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
virtualenv -p python3.6 venv
```

Поднимаем базу данных  с помощью докера

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
# Работа с базой данных
init базы

```bash
flask db init
```
migrate базы

```bash
flask db migrate
```
upgrade базы(если нужно)

```bash
flask db upgrade
```
# Запуск сервера


```bash
flask run
```
# Запуск тестов


```bash
python -m unittest
```