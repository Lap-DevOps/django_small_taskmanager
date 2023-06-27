from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField('Short task name', max_length=50)
    task = models.TextField('Task description', max_length=500)
    date_added = models.DateField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    date_finished = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
