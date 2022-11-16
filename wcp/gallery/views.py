from django.shortcuts import render
from .models import Gallery


def gallery(request):
    gallery = Gallery.objects.all()
    g_slider = Gallery.objects.all().order_by('-date_p')[:5]
    context = {
        'gallery': gallery,
        'title': 'Список новостей',
        'slider': g_slider,
    }
    return render(request, 'gallery/gallery.html', context)


