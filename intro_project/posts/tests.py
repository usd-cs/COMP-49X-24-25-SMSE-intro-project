"""
Test module for the Post and Comment models in the posts app.
Includes tests for creating and validating the models.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment
from unittest import skip
#from unittest.mock import patch, MagicMock


class PostModelTest(TestCase):
    """ 
    Test case for the Post model.
    """
    @skip("Skipping this test temporarily.")
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

    @skip("Skipping this test temporarily.")
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
    @skip("Skipping this test temporarily.")
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

    @skip("Skipping this test temporarily.")
    def test_comment_creation(self):
        """
        Checks that the Comment instance was created successfully.
        """
        self.assertEqual(self.comment.content, "Test comment content")
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author.username, "testcommenter")
        self.assertIsInstance(self.comment, Comment)

class PostCreateViewTest(TestCase):
    """
    Test case for the post creation view.
    """
    def setUp(self):
        """
        Sets up a test user and the route for testing.
        """
        self.user = User.objects.create_user(username="testuser", password="password")
        self.url = reverse("posts:create_post")  # makes sure that the URL name matches whats in the urls.py

    def test_create_post_logged_in(self):
        """
        Test creating a post while logged in.
        """

        user_exists = User.objects.filter(username="testuser").exists()
        self.assertTrue(user_exists, "Test user does not exist in the database")

        logged_in = self.client.login(username="testuser", password="password")
        self.assertTrue(logged_in, "Login failed for testuser")

        data = {
            "title": "Test Post",
            "content": "This is a test post content while logged in.",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201) #succesful
        self.assertTrue(Post.objects.filter(title="Test Post").exists())


    def test_create_post_not_logged_in(self):
        """
        Test creating a post while not logged in.
        """
        data = {
            "title": "Test Post",
            "content": "This is a test post content while not logged in.",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302) #redirects to login page by default
        self.assertFalse(Post.objects.filter(title="Test Post").exists())

    def test_create_post_missing_data(self):
        """
        Test creating a post with missing data fields.
        """
        self.client.login(username="testuser", password="password")
        data = {"title": ""}  # shows missing fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)  # 400 Bad Request (client error response)
        self.assertFalse(Post.objects.filter(title="").exists())
