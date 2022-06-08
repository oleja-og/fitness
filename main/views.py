from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'rules.html')


def index3(request):
    return render(request, 'shedule.html')


def index4(request):
    return render(request, 'contact.html')
