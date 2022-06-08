from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='blog_equipment', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Equipment'
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
        ordering = ('-created',)


    def __str__(self):
        return self.title