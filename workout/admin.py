from django.contrib import admin
from .models import Workout, WorkoutVideo

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'gender')


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutVideo)
