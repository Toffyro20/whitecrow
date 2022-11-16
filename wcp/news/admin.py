from django.contrib import admin
from .models import News, CatNews


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_p', 'date_u')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'short_d')
    list_filter = ('category',)


class CatNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(CatNews, CatNewsAdmin)

