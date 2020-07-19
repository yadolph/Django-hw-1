from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    current_time = current_time.strftime('Текущая дата: %d-%m-%Y, время: %H:%M:%S')
    return HttpResponse(current_time)


def workdir_view(request):
    ldir = listdir(path='.')
    paragraph = '<p/>'
    msg = paragraph.join(ldir)
    return HttpResponse(msg)