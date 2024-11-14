"""
Url file configuration

Defines the URLs for the app and connects each url to its corresponding view.
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "posts"

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/comment/', views.create_comment, name='create_comment'),

]
