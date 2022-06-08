from django.shortcuts import render

import datetime
from django.utils import timezone as tz
from django.views.generic import ListView
from .models import Shedule


class SheduleListView(ListView):
    queryset = Shedule.objects.all()
    template_name = 'shedule.html'
    context_object_name = 'shedule'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        plus = datetime.timedelta(days=1)


        next = now+plus
        ctx['plus'] = plus
        ctx['now'] = now
        ctx['today'] = datetime.datetime.today().strftime("%d.%m.%Y.%A")
        ctx['next'] = next.strftime("%d.%m.%Y.%A")
        return ctx


