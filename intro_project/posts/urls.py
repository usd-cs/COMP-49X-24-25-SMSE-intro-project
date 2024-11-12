"""
Url fil
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"), #home page
    path('create_post/', views.create_post, name='create_post')
    #path('create_posts/', views.create_post, name='create_posts'),
]
