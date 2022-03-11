from unicodedata import name
from django.contrib import admin
from django.http.response import HttpResponse

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('news/<str:pk>', views.news, name="news"),
    path('nation/',views.nation, name="nation"),

    path('create-news/',views.createNews, name="create-news"),
    path('update-news/<str:pk>', views.updateNews, name="update-news"),

    path('delete-news/<str:pk>', views.deleteNews, name="delete-news"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 