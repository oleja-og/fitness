from django.db import models

class Rules(models.Model):
    title = models.CharField(max_length=50, verbose_name="Правила клуба")
    rules = models.TextField()


    class Meta:
        db_table = "Rules"
        verbose_name = "Правила"
        verbose_name_plural = "Правила"

    def __str__(self):
        return self.title



class Contacts(models.Model):
    title = models.CharField(max_length=50, verbose_name="Контакты")
    name = models.CharField(max_length=50, verbose_name="Название клуба")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house = models.IntegerField(verbose_name="Дом")
    phone = models.CharField(max_length=13, help_text="375_________", verbose_name="Тел.")
    email = models.EmailField()
    bank = models.TextField(verbose_name="Реквизиты")


    class Meta:
        db_table = "Contacts"
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.title