from django.db import models
from django.contrib.auth.models import User
from services.models import Services

class Trainers(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    date = models.DateField(verbose_name="Дата рождения")
    phone = models.CharField(max_length=13, help_text="375_________", verbose_name="Тел.")
    salary = models.IntegerField(verbose_name="Оклад")
    addres = models.CharField(max_length=200, verbose_name="Описание")
    image = models.ImageField(upload_to='static/img/')

    class Meta:
        db_table = "Trainers"
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"


    def __str__(self):
        return f"{self.name} {self.last_name}"


class Trainers_spec(models.Model):
    employee_number = models.ForeignKey(Trainers, on_delete=models.CASCADE, verbose_name="Номер сотрудника")
    service_number = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуги")
    note = models.CharField(max_length=100, verbose_name="Примечание")


    class Meta:
        db_table = "Services_spec"
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

    def __str__(self):
        return f"{self.employee_number} {self.service_number}"