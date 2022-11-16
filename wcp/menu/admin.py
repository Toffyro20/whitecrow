from django.contrib import admin
from .models import Menu, CatMenu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'categoryM')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'contacts', 'title')
    list_filter = ('categoryM',)


class CatMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(CatMenu, CatMenuAdmin)
