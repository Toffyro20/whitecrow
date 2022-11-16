from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='photo_m/%Y/%m/%d/', verbose_name='Фото')
    text_n = models.TextField(verbose_name='Описание')
    categoryM = models.ForeignKey('CatMenu', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('menudesc', kwargs={'menu_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['title']


class CatMenu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категории меню', db_index=True)

    def get_absolute_url(self):
        return reverse('menuCategory', kwargs={'categoryM_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'
        ordering = ['title']