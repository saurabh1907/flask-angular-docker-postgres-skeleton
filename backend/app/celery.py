from celery import Celery
from app import app, Blog
from app.views.views import blog_service

celery = Celery(__name__, backend=app.config['CELERY_BACKEND'], broker=app.config.CELERY_BROKER_URL)
celery.conf.update(app.config)

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask


@celery.task()
def add_dummy_blogs(count, duration):
    for i in range(0, count):
        blog_service.save(Blog("A blog from Celery", "A content from Celery"))
    return "Task Complete"


# celery -A your_application.celery worker
