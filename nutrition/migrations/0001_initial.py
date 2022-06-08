# Generated by Django 4.0.4 on 2022-06-04 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('woman', 'Woman')], max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_nutrition', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Питание',
                'verbose_name_plural': 'Питание',
                'db_table': 'Nutrition',
                'ordering': ('-created',),
            },
        ),
    ]
