"""
Models for the 'posts' application.

Defines the `Post` and `Comment` models.
"""

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        content (str): The content/body of the post.
        author (User): The user who authored the post.
        created_at (datetime): The timestamp when the post was created.
    """
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Attributes:
        post (Post): The post to which the comment belongs.
        author (User): The user who authored the comment.
        content (str): The content/body of the comment.
        created_at (datetime): The timestamp when the comment was created.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
