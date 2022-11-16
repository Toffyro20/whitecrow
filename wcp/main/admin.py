from django.contrib import admin
from .models import Main


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_c', 'phone_n', 'date_b', 'time_b', 'table_b', 'clients_n')
    list_display_links = ('id', 'name_c')
    search_fields = ('name_c', 'phone_n', 'date_b')


admin.site.register(Main, MainAdmin)

