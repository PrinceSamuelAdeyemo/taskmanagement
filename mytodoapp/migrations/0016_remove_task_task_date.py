# Generated by Django 4.1.1 on 2023-01-07 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodoapp', '0015_alter_task_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_date',
        ),
    ]
