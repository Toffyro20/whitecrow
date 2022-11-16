from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contacts', 'description')
    list_display_links = ('id', 'title', 'contacts')
    search_fields = ('id', 'contacts', 'title')


admin.site.register(About, AboutAdmin)
