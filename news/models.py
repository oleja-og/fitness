from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=250)
    about = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/')
    author = models.ForeignKey(User, related_name='news', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'News'
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-publish',)

    def __str__(self):
        return self.title
