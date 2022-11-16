from django.shortcuts import render, redirect
from .models import Main
from .forms import MainForm
from news.models import News, CatNews


def main(request):
    news_item = News.objects.all().order_by('-date_p')[:1]
    errordb = ''
    errorv = ''
    main = Main.objects.all()
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            errorv = 'Введены некорректные данные'


    form = MainForm()
    context = {
        'main': main,
        'title': 'Список новостей',
        'form': form,
        'errordb': errordb,
        'errorv': errorv,
        'news_item': news_item,
    }

    return render(request, 'main/main.html', context)


