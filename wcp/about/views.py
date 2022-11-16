from django.shortcuts import render
from .models import About


def about(request):
    about = About.objects.all()
    context = {
        'about': about,
        'title': 'Список новостей',
    }
    return render(request, 'about/about.html', context)

