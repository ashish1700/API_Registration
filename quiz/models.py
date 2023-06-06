from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
# from .tasks import delete_expired_objects
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta


# Create your models here.



class Videoo(models.Model):
    name = models.CharField(max_length=255)
    # video = models.FileField(upload_to='videos/')
    video = models.FileField(null=True, 
                           blank=True, upload_to='videos/', 
                           validators=[FileExtensionValidator( ['MP4'] ) ])
    thumbnail = models.ImageField(null=True, 
                           blank=True,upload_to='thumbnails/', 
                           validators=[FileExtensionValidator( ['PNG', 'JPEG'] ) ])
    expiry_time = models.DateTimeField()

    def __str__(self):
        return self.name
@receiver(post_save, sender=Videoo)
def schedule_video_deletion(sender, instance, created, **kwargs):
    if created:
        current_time = timezone.now()
        time_difference = instance.expiry_time - current_time
        delete_expired_videos.apply_async(countdown=time_difference.total_seconds())


class Questions(models.Model):
    
    video = models.ForeignKey(Videoo, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=255)
    option1 = models.ImageField(null=True, 
                           blank=True, upload_to='images/', 
                           validators=[FileExtensionValidator( ['PNG', 'JPEG'] ) ])
    option2 = models.ImageField(null=True, 
                           blank=True, upload_to='images/', 
                           validators=[FileExtensionValidator( ['PNG', 'JPEG'] ) ])
    answer= models.PositiveIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2')])
    
    def __str__(self):
        return self.question
    # update_time = models.DateTimeField(auto_now=True)
    
    


class VideoFestival(models.Model):
    video_festival_name = models.CharField(max_length=1000)
    video_festival = models.FileField(upload_to='video/festival', null=True, blank=True)
    thumbnail_image = models.FileField(upload_to='image/festival', null=True, blank=True)
    
    
    def __str__(self):
        return self.video_festival_name




 
    
# class Category(models.Model):
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name
        
        
# class Quizzes(models.Model):
    
#     class Meta:
#         verbose_name = _("Quiz")
#         verbose_name_plural = _("Quizzes")
#         ordering = ['id']
    
#     title = models.CharField(max_length=255, default =_("new quiz"), verbose_name=_("Quiz Title"))
    
#     category = models.ForeignKey(
#         category, default=1, on_delete =models.DO_NOTHING)
    
# class Question(UpdatedQuestion):
#     quiz = models.ForeignKey(
#         Quizzes, related_name='question', on_delete=models.DO_NOTHING)

# class Answer(UpdatedQuestion):
#     Question = models.Foreignkey(
#         question, related_name='answer', on_delete = models.DO_NOTHING
#     )
    
class Testing_image(models.Model):
    name = models.CharField(max_length=199)
    image = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # @property
    # def deletes_in_ten_seconds(self):
    #     time = self.created_at + timedelta(seconds=10)
    #     query = Testing_image.objects.get(pk=self.pk)
    #     if time > now():
    #         query.delete()
    @property
    def deletes_in_ten_seconds(self):
        time = self.created_at + timedelta(seconds=10)
        if time > timezone.now():
            self.delete()
    