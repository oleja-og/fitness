from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('woman', 'Woman'),
    )
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='blog_workout', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/')
    video = models.ImageField(upload_to='static/movie/', null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'Workout'
        verbose_name = "Не заполнять"
        verbose_name_plural = "Не заполнять"
        ordering = ('-created',)

    def __str__(self):
        return self.title


class WorkoutVideo(Workout):
    url = models.URLField()

