# import os
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
# settings.configure()
# from celery import Celery

# # Instantiate the Celery application
# app = Celery('task')

# # Load the celery configurations from your Django settings
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Discover tasks in all Django apps
# app.autodiscover_tasks()

# # Move the CELERY_BEAT_SCHEDULE inside app.conf.beat_schedule
# app.conf.beat_schedule = {
#     'delete-expired-objects': {
#         'task': 'quiz.tasks.delete_expired_objects',
#         'schedule': 60,  # Run the task every minute
#     },
# }









# import os
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
# settings.configure()
# from celery import Celery

# # Instantiate the Celery application
# app = Celery('task')

# # Load the celery configurations from your Django settings
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Discover tasks in all Django apps
# app.autodiscover_tasks()

# CELERY_BEAT_SCHEDULE = {
#     'delete-expired-objects': {
#         'task': 'quiz.tasks.delete_expired_objects',
#         'schedule': 60,  # Run the task every minute
#     },
# }