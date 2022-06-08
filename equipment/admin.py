from django.contrib import admin
from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')


admin.site.register(Equipment, EquipmentAdmin)