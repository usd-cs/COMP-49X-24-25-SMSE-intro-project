"""
Url file
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "posts"

urlpatterns = [
    path("", views.home, name="home"), #home page
    path('create_post/', views.create_post, name='create_post'),
    #path('create_posts/', views.create_post, name='create_posts'),
]
