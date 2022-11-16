from django.contrib import admin

from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'media', 'date_p')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(Gallery, GalleryAdmin)
