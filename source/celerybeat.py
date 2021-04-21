from main import app
from celery import Celery


def run_celery(app):
    celery = Celery('sanic', backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL']
    )

    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = run_celery(app)
