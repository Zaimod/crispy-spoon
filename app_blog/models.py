# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category = models.CharField(u'Category', max_length=250, help_text=u'Must be less than 250 characters')
    slug = models.SlugField(u'Slug')
    objects = models.Manager()

    class Meta:
        verbose_name = u'Category for article'
        verbose_name_plural = u'Categories for articles'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('article-category-list', kwargs={'slug': self.slug})
        except:
            url = "/"

        return url
    


class Article(models.Model):
    title = models.CharField(u'Title', max_length=250, help_text=u'Must be less than 250 characters')
    description = models.TextField(blank=True, verbose_name=u'Description')
    date_of_publication = models.DateTimeField(u'Date of publication', default=timezone.now)
    slug = models.SlugField(u'Slug', unique_for_date='date_of_publication')
    main_page = models.BooleanField(u'Main', default=False, help_text=u'Show on main page')
    category = models.ForeignKey(Category, related_name='articles', blank=True, null=True, verbose_name=u'Category',
                                 on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ['-date_of_publication']
        verbose_name = u'Article'
        verbose_name_plural = u'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            url = reverse('news-detail',
                          kwargs={
                              'year': self.date_of_publication.name.strfitime("%Y"),
                              'month': self.date_of_publication.name.strftime("%m"),
                              'day': self.date_of_publication.name.strftime("%d"),
                              'slug': self.slug,
                          })
        except:
            url = "/"
        return url


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name=u'Article', related_name=u'images', on_delete=models.CASCADE)
    image = models.ImageField(u'Image', upload_to='photos')
    title = models.CharField(u'Title', max_length=250, help_text=u'Must be less than 250 characters')

    class Meta:
        verbose_name = u'Image for article'
        verbose_name_plural = u'Images for article'

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]
