"""
Url file configuration

Defines the URLs for the app and connects each URL to its corresponding view.
"""
from django.urls import path
from . import views

app_name = "posts"

# Define the URL patterns for the 'posts' app
urlpatterns = [
    # Home page to display all posts
    path('', views.home, name='home'),

    # Create a new post
    path('create/', views.create_post, name='create_post'),

    # Add a comment to a specific post
    path('<int:post_id>/comment/', views.create_comment, name='create_comment'),

    # Delete a specific post (accessible only to superusers)
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),

    # Delete a specific comment (accessible only to superusers)
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
