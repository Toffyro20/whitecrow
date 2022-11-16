from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name="menu"),
    path('menu_category/<int:categoryM_id>/', views.get_menuCategory, name="menuCategory"),
    path('menu/<int:menu_id>/', views.get_menu, name="menudesc"),
]