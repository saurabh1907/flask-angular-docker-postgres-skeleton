from app import celery, create_app
from app.models.blog import Blog
from app.views.views import blog_service
from flask_cors import CORS


@celery.task()
def add_dummy_blogs(count, duration):
    for i in range(0, count):
        blog_service.save(Blog("A blog from Celery", "A content from Celery"))
    return "Task Complete"

app = create_app(env='celery')
CORS(app, origins='*')
# app.app_context().push()


# Run Using
# celery -A app.celery.celery_worker.celery worker --loglevel=info
