from django.contrib.auth.models import User
from django.db import models


class Sportroom(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название", unique=True)


    class Meta:
        db_table = "Sportroom"
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"

    def __str__(self):
        return self.name