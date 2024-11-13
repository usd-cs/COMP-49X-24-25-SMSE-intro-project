"""
Url fil
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "posts"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"), #home page
    path('create_post/', views.create_post, name='create_post'),
    path("login/", auth_views.LoginView.as_view(template_name="posts/login.html"), name="login"),  # Login page
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),  # Logout and redirect to home
    #path('create_posts/', views.create_post, name='create_posts'),
]
