from django.contrib import admin
from app1.models import task
# Register your models here.


@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display=('id','uname','email','password','user_type')