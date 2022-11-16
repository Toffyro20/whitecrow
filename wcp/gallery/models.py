from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название фото')
    media = models.ImageField(upload_to='photo_g/%Y/%m/%d/', verbose_name='Фото')
    date_p = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        ordering = ['-date_p']
