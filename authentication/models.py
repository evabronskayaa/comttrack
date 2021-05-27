from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.urls import reverse


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
        return f"{self.first_name} {self.last_name} - {self.department}"


class Task(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название задачи")
    description = models.CharField(max_length=200, verbose_name="Описание задачи")
    task_setter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Составитель задачи",
                                    related_name='user_setter')
    executor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Исполнитель",
                                 related_name='user_executor')
    completed = models.BooleanField(default=False, verbose_name="Выполнена")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}. От {self.task_setter} для {self.executor}"

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.pk})


class Notification(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Создатель уведомления",
                               related_name="notification_author")
    text = models.CharField(max_length=150, verbose_name="Текст уведомления")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.text}"
