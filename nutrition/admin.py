from django.contrib import admin
from .models import Nutrition


class NutritionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'gender')


admin.site.register(Nutrition, NutritionAdmin)