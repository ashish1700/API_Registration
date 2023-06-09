# Generated by Django 4.2 on 2023-06-05 09:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testing_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199)),
                ('image', models.FileField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_festival_name', models.CharField(max_length=1000)),
                ('video_festival', models.FileField(blank=True, null=True, upload_to='video/festival')),
                ('thumbnail_image', models.FileField(blank=True, null=True, upload_to='image/festival')),
            ],
        ),
        migrations.CreateModel(
            name='Videoo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(['MP4'])])),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/', validators=[django.core.validators.FileExtensionValidator(['PNG', 'JPEG'])])),
                ('expiry_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('option1', models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['PNG', 'JPEG'])])),
                ('option2', models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['PNG', 'JPEG'])])),
                ('answer', models.PositiveIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2')])),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.videoo')),
            ],
        ),
    ]
