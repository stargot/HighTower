import datetime
from django.db import models


# Create your models here.
class Host(models.Model):
    host_name = models.CharField('Name', max_length=100)
    port = models.PositiveSmallIntegerField('Port', default=80)
    status = models.BooleanField('Status', default=True)
    created = models.DateTimeField("Добавлен", default=datetime.datetime.now)
    updated = models.DateTimeField("Обновлен", auto_now=True)

    class Meta:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'
        ordering = ["-created"]

    def __str__(self):
        return self.host_name
