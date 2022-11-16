from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('category/<int:category_id>/', views.get_category, name="category"),
    path('news/<int:news_id>/', views.get_news, name="newsdesc"),
]


