from .server import app as server_app
from datetime import timedelta
from celery import Celery
import asyncio
from .test_data import order_pallet_data
from app.views.celery import send_gls_task


# MAKE CELERY
def make_celery(server_app):
    celery = Celery(
        server_app,
        broker=server_app.config['CELERY_BROKER_URL'],
        backend=server_app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(server_app.config)
    celery.autodiscover_tasks()

    celery.conf.CELERYBEAT_SCHEDULE = {
        'send_fake_order_pallet_data': {
            'task': 'send_fake_data',
            'schedule': timedelta(seconds=5),
            'kwargs': order_pallet_data
        },
    }
    return celery


# CELERY RUN
celery = make_celery(server_app)


# TASKS
@celery.task(name='send_fake_data')
def send_fake_data(**kwargs):
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.get_event_loop().run_until_complete(send_gls_task(**kwargs))
