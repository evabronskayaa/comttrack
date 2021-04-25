from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    department = models.CharField(max_length=30, verbose_name="Отдел")
    status = models.CharField(max_length=10, verbose_name="Должность")

    def __str__(self):
        return self.username
