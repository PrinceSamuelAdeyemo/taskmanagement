# Generated by Django 4.1.1 on 2022-12-02 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mytodoapp', '0007_alter_task_task_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessprofile',
            name='businessTask',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='personalTask',
        ),
        migrations.AddField(
            model_name='task',
            name='businessTaskowner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mytodoapp.businessprofile'),
        ),
        migrations.AddField(
            model_name='task',
            name='personalTaskowner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mytodoapp.profile'),
        ),
    ]
