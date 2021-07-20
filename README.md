# SanicSeleryServer

Copy `example.env` in `.env`

```bash
cp example.env .env
```

Change `.env`s `SECRET_KEY`

Install vurtual environment

```bash
virtualenv python3.7 -m venv venv
```

Up db and docker-compose

```bash
docker-compose up -d
```

activate venv

```bash
source venv/bin/activate
```

install requirements

```bash
pip install -r requirements.txt
```

# Runserver

```bash
python manage.py run

```
# run celery (from backend/ directory)
```bash
celery -A celery.celery worker -B -l INFO 
опционально:
...INFO --loglevel=DEBUG
```

# Run tests (still not working)

```bash
python -m unittest
```

