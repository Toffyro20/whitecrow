from django.shortcuts import render
from .models import Menu, CatMenu


def menu(request):
    menu = Menu.objects.all()
    categoriesm = CatMenu.objects.all()
    context = {
        'menu': menu,
        'title': 'Список новостей',
        'categoriesm': categoriesm,
    }
    return render(request, 'menu/menu.html', context)


def get_menuCategory(request, categoryM_id):
    menu = Menu.objects.filter(categoryM_id = categoryM_id)
    categoriesm = CatMenu.objects.all()
    categorym = CatMenu.objects.get(pk=categoryM_id)
    return render(request, 'menu/menu_category.html', {'menu': menu, 'categorym': categorym, 'categoriesm': categoriesm})


def get_menu(request, menu_id):
    menu_item = Menu.objects.get(pk=menu_id)
    return render(request, 'menu/view_menu.html', {'menu_item': menu_item})



