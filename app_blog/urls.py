from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
