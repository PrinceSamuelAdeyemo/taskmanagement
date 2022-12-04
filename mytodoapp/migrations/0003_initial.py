# Generated by Django 4.1.1 on 2022-12-01 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mytodoapp', '0002_remove_businessprofile_businesstask_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('subtask_name', models.CharField(max_length=200)),
                ('subtask_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('subtask_done', models.BooleanField(default=False)),
                ('subtask_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_name', models.CharField(max_length=150)),
                ('task_description', models.TextField(default=None)),
                ('task_file', models.FileField(default=None, upload_to='task_file_folder')),
                ('task_image', models.ImageField(default=None, upload_to='task_image_folder')),
                ('task_done', models.BooleanField(default=False)),
                ('task_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('task_date', models.DateField()),
                ('subtask', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mytodoapp.subtask')),
                ('task_owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_profile', models.IntegerField()),
                ('personalTask', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mytodoapp.task')),
                ('personal_basicdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessprofile_id', models.IntegerField()),
                ('businessTask', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mytodoapp.task')),
                ('business_basicdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
