"""
App configuration file for the posts app.
"""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """
    This is the Appconfig for posts.
    This class specifies the defauly auto field type and name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
