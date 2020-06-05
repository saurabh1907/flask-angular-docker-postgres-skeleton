from app import celery, app_setting, create_app
from app.celery import init_celery
from app.models.blog import Blog
from app.views.views import blog_service


@celery.task()
def add_dummy_blogs(count, duration):
    print("from task")
    for i in range(0, count):
        blog_service.save(Blog("A blog from Celery", "A content from Celery"))
    return "Task Complete"

app = create_app(app_setting)
# app.app_context().push()
# init_celery(celery, app)
