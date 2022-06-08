from django.contrib import admin
from .models import Rules, Contacts


class RulesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'city')


admin.site.register(Rules, RulesAdmin)
admin.site.register(Contacts, ContactsAdmin)
