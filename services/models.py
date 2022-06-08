from django.db import models
from django.contrib.auth.models import User


class Services(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название услуги", unique=True)
    image = models.ImageField(upload_to='static/img/')
    about = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        db_table = "Services"
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Card(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название абонемента", unique=True)
    price = models.IntegerField(verbose_name="Цена")
    number_of_visits = models.IntegerField(verbose_name="Количество посещений")
    number_of_days = models.IntegerField(verbose_name="Количество дней")

    class Meta:
        db_table = "Card"
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"

    def __str__(self):
        return self.name


class Card_sale(models.Model):
    client_code = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Код клиента")
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name="абонемент клиента")
    start_date = models.DateField(auto_now_add=True, verbose_name="Дата начала")
    finish_date = models.DateField(verbose_name="Дата окончания")

    class Meta:
        db_table = "Card_sale"
        verbose_name = "Продажа абонемента"
        verbose_name_plural = "Продажа абонементов"

    def __str__(self):
        return f"{self.client_code} {self.card}"
