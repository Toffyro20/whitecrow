from django.db import models


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название контакта')
    contacts = models.CharField(max_length=250, verbose_name='Контакты')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.contacts

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['title']

