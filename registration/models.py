from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBasedModel):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    username = models.CharField(max_length=20, verbose_name="Имя пользователя")
    department = models.CharField(max_length=20, verbose_name="Отдел")
    role = models.CharField(max_length=10, verbose_name="Должность")
    password = models.BinaryField(verbose_name="Пароль")
    is_deleted = models.BooleanField(default=False, verbose_name="Удален")
