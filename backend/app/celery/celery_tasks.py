# from app import celery
# from app.models.blog import Blog
# from app.views.views import blog_service
#
#
# @celery.task()
# def add_dummy_blogs(count, duration):
#     print("from task")
#     for i in range(0, count):
#         blog_service.save(Blog("A blog from Celery", "A content from Celery"))
#     return "Task Complete"

# Start Celery when deploying flask locally
# celery worker -A app.celery.celery --loglevel=info
# celery -A myflaskapp.celery beat -l info
