from celery import Celery

# Celery is dynamically initialized in run.py
celery_client = Celery()

def create_celery(app):
    celery = Celery(app.import_name, broker='redis://localhost:6379/0')
    celery.conf.update(app.config)
    # celery_client.config_from_object(app.config)
    TaskBase = celery.Task

    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


from app.views.views import blog_service

@celery_client.task()
def add_dummy_blogs(count, duration):
    print("from task")
    # for i in range(0, count):
    blogs = blog_service.all()
    # blog_service.save(Blog("A blog from Celery", "A content from Celery"))
    return "Task Complete"


# Start Celery when deploying flask locally
# celery worker -A app.celery.celery --loglevel=info
# celery -A myflaskapp.celery beat -l info
