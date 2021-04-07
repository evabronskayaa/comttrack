# Generated by Django 3.1.7 on 2021-04-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('department', models.CharField(max_length=20, verbose_name='Отдел')),
                ('role', models.CharField(max_length=10, verbose_name='Должность')),
                ('password', models.BigIntegerField(max_length=100, verbose_name='Пароль')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
