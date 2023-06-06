from django.db import models

# Create your models here.


class Video1(models.Model):
    # caption=models.CharField(max_length=100)
    agegroup = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    video =models.FileField(upload_to="video/%y")
    # def __str__(self):
    #     return self.caption
    
    
# class APItest(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')
#     age = models.CharField(max_length=20 ,blank=True)
#     email= models.EmailField(max_length=255)
#     mobileno = models.CharField(max_length=15)
