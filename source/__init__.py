import contextlib


# FIND .ENV VARS
with contextlib.suppress(ImportError):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())


# CELERY RUN
from .celerybeat import celery as celery_app

__all__ = ('celery_app',)
