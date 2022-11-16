from django.db import models


class Main(models.Model):
    name_c = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone_n = models.CharField(max_length=12, verbose_name='Номер телефона')
    date_b = models.DateField(verbose_name='Дата бронирования')
    time_b = models.TimeField(verbose_name='Время бронирования')
    table_b = models.CharField(max_length=2, verbose_name='Номер стола')
    clients_n = models.CharField(max_length=2, verbose_name='Количество клиентов')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
        ordering = ['-date_b', '-time_b']

