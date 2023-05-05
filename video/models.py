from django.db import models

# Create your models here.


class Video(models.Model):
    # caption=models.CharField(max_length=100)
    agegroup = models.CharField(max_length=200, default='DEFAULT VALUE')
    subject = models.CharField(max_length=200, default='DEFAULT VALUE')
    topic = models.CharField(max_length=200, default='DEFAULT VALUE')
    video=models.FileField(upload_to="video/%y", default='DEFAULT VALUE')
    # def __str__(self):
    #     return self.caption
    
    
# class APItest(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')
#     age = models.CharField(max_length=20 ,blank=True)
#     email= models.EmailField(max_length=255)
#     mobileno = models.CharField(max_length=15)
