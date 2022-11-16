# Generated by Django 4.1.3 on 2022-11-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Категории новостей')),
            ],
            options={
                'verbose_name': 'Категория новости',
                'verbose_name_plural': 'Категории новостей',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('short_d', models.CharField(max_length=300, verbose_name='Краткое описание')),
                ('date_p', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('date_u', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('photo', models.ImageField(blank=True, upload_to='photo_n/%Y/%m/%d/', verbose_name='Фото')),
                ('text_n', models.TextField(verbose_name='Текст')),
                ('category.html', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.catnews', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date_p'],
            },
        ),
    ]
