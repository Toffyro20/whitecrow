from django.shortcuts import render
from .models import News, CatNews


def news(request):
    news = News.objects.all().order_by('-date_p')
    categories = CatNews.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, 'news/news.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    categories = CatNews.objects.all()
    category = CatNews.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category, 'categories': categories})


def get_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})
