from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    short_d = models.CharField(max_length=300, verbose_name='Краткое описание')
    date_p = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    date_u = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    photo = models.ImageField(upload_to='photo_n/%Y/%m/%d/', blank=True, verbose_name='Фото')
    text_n = models.TextField(verbose_name='Текст')
    category = models.ForeignKey('CatNews', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('newsdesc', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_p']


class CatNews(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категории новостей', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'
        ordering = ['title']