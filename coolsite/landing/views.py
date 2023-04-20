from time import time

from django.shortcuts import render, redirect
from .forms import Clients_phone
from .models import Client


def index(request):
    context = {
        'title': 'Главная страница - Dj Neo',
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'Event DJ'
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':

        form = Clients_phone(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('thanks')
    else:
        form = Clients_phone()
    return render(request, 'contact.html', {'form': form, 'title': "Заказать лучшую дискотеку"})


def work(request):
    context = {
        'title': 'Диджей на свадьбу'
    }
    return render(request, 'work.html', context)


def secret_master(request):
    context = {
        'title': 'Корпоратив - Русская дискотека'
    }
    return render(request, 'blog.html', context)


def thanks(request):
    context = {
        'title': 'Мы с вами свяжемся'
    }
    return render(request, 'thanks.html', context)


def work_single(request):
    context = {
        'title': 'Свадьба только раз...'
    }
    return render(request, 'work-single.html', context)


def blog(request):
    context = {
        'title': 'Секреты'
    }
    return render(request, 'blog.html', context)


def blog_single(request):
    context = {
        'title': 'Блог'
    }
    return render(request, 'blog-single.html', context)


def reviews(request):
    context = {
        'title': 'Отзывы о Диджее'
    }
    return render(request, 'reviews.html', context)
