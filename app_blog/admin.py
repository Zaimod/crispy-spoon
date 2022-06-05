# -*- coding: utf-8 -*-

from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        ('', {
            'fields': ('category',),
        }),
        (u'Additional', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        })
    )
    prepopulated_fields = {'slug': ('category',)}


admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0

    fieldsets = (
        ('', {
            'fields': ('title', 'image',),
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_publication', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fieldsets = (
        ('', {
            'fields': ('date_of_publication', 'title', 'description', 'main_page'),
        }),
        (u'Additional', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        })
    )

    @staticmethod
    def delete_file(pk):
        """Delete an image."""

        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()


admin.site.register(Article, ArticleAdmin)
