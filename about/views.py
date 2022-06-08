from .models import Rules, Contacts
from django.views.generic import ListView


class RulesListView(ListView):
    queryset = Rules.objects.all()
    template_name = "rules.html"
    context_object_name = 'rules'


class ContactsListView(ListView):
    queryset = Contacts.objects.all()
    template_name = "contact.html"
    context_object_name = 'contact'
