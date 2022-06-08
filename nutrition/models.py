from django.db import models
from django.contrib.auth.models import User


class Nutrition(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('woman', 'Woman'),
    )
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='blog_nutrition', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'Nutrition'
        verbose_name = "Питание"
        verbose_name_plural = "Питание"
        ordering = ('-created',)

    def __str__(self):
        return self.title
