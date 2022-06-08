from django.db import models
from django.contrib.auth.models import User
from main.models import Sportroom
from trainers.models import Trainers
from services.models import Services, Card_sale


class Shedule(models.Model):
    data = models.DateField(verbose_name="Дата")
    time_start = models.TimeField(verbose_name="Начало тренировки")
    time_finish = models.TimeField(verbose_name="Конец тренировки")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуга")
    sportroom = models.ForeignKey(Sportroom, on_delete=models.CASCADE, verbose_name="Помещение")
    staff = models.ForeignKey(Trainers, on_delete=models.CASCADE, verbose_name="Персонал")
    note = models.CharField(max_length=100, verbose_name="Примечание")

    class Meta:
        db_table = "Shedule"
        verbose_name = "Расписание"

    def __str__(self):
        return f'{self.data} {self.service} {self.time_start}'


class Visitation_record(models.Model):
    card_number = models.ForeignKey(Card_sale, on_delete=models.CASCADE, verbose_name="Номер карты")
    namber_shedule = models.ForeignKey(Shedule, on_delete=models.CASCADE, verbose_name="№ по расписанию")

    class Meta:
        db_table = "Visitation_record"
        verbose_name = "Запись о посещении"
        verbose_name_plural = "Записи о посещениях"

    def __str__(self):
        return f"{self.card_number}"