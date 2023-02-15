# Generated by Django 4.1.1 on 2023-01-06 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mytodoapp', '0013_board_remove_task_businesstaskowner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='task_file_folder'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='task_image_folder'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_inprogress',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_assign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mytodoapp.profile'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_owner',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_owner',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
