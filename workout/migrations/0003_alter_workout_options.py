# Generated by Django 4.0.4 on 2022-06-08 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_workoutvideo_alter_workout_image_alter_workout_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ('-created',), 'verbose_name': 'Не заполнять', 'verbose_name_plural': 'Не заполнять'},
        ),
    ]
