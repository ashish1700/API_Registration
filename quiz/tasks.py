# from celery import shared_task
# from django.utils import timezone
# from .models import Videoo
# from task.celery import ap



# @shared_task
# def delete_expired_objects():
#     expired_objects = Videoo.objects.filter(expiry_time__lt=timezone.now())
#     expired_objects.delete()