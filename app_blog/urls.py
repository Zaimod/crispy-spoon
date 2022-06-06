from django.urls import path
from django.conf import settings
from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)
from django.conf.urls.static import static
urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
    path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)