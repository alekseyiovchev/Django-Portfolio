from django.urls import reverse
from django.db import models


# Create your models here.
class Stack(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")
    content = models.TextField(blank=True,verbose_name='Контент')
    wiki = models.URLField(null=True,verbose_name='Википедия')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    done = models.BooleanField(default=True,verbose_name= 'Изученно')
    cat = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Категория')

    class Meta:
        verbose_name ='Технология (Stack)'
        verbose_name_plural ='Технологии'
        ordering = ['time_create','title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug}) 

class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name = 'Название категории')
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name='Слаг')

    class Meta:
        verbose_name ='Категория'
        verbose_name_plural ='Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_slug':self.slug}) 