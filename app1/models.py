from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

USER_TYPE_CHOICES = (
            ('superadmin', 'Super Admin'),
            ('admin', 'Admin'),
            ('student', 'Student'),
        )



class task(models.Model):
    uname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
def __str__(self):
    return self.uname