"""
Test module for the Post and Comment models in the posts app.
Includes tests for creating and validating the models.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
#from unittest.mock import patch, MagicMock

class PostModelTest(TestCase):
    """ 
    Test case for the Post model.
    """
    def setUp(self):
        """
        Set up a test user and a post instance for testing.
        """
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(
            title="Test Creating Post",
            content="Test post content",
            author=self.user
        )

    def test_post_creation(self):
        """
        Checks that the Post instance was successfully created.
        """
        self.assertEqual(self.post.title, "Test Creating Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertIsInstance(self.post, Post)

class CommentModelTest(TestCase):
    """
    Test case for the Comment model.
    """
    def setUp(self):
        """
        Sets up a test user, post, and a comment instance for testing.
        """
        self.user = User.objects.create_user(username="testcommenter", password="password")
        self.post = Post.objects.create(
            title="Test Comment",
            content="Test post content",
            author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post,
            content="Test comment content",
            author=self.user
        )

    def test_comment_creation(self):
        """
        Checks that the Comment instance was created successfully.
        """
        self.assertEqual(self.comment.content, "Test comment content")
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author.username, "testcommenter")
        self.assertIsInstance(self.comment, Comment)
