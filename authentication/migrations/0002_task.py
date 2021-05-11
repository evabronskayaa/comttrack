# Generated by Django 3.2 on 2021-04-30 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название задачи')),
                ('description', models.CharField(max_length=200, verbose_name='Описание задачи')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнена')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_executor', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('task_setter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_setter', to=settings.AUTH_USER_MODEL, verbose_name='Составитель задачи')),
            ],
        ),
    ]