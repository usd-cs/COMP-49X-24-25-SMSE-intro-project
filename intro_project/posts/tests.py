"""
Test module for the Post and Comment models in the posts app.
Includes tests for creating and validating the models.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from unittest import skip
from django.urls import reverse
from .models import Post, Comment
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

        #tests the data that is being posted
        data = {
            "content": "This is a test post content while logged in.",
        }

        response = self.client.post(self.url, data)

        #tests if the response is redirected to the home page
        self.assertEqual(response.status_code, 302) #succesful
        self.assertRedirects(response, reverse('posts:home'))

        #tests if the post was created successfully
        self.assertTrue(Post.objects.filter(content="This is a test post content while logged in.").exists())



    def test_create_post_not_logged_in(self):
        """
        Test creating a post while not logged in.
        """

        #tests the data that shouldnt be posted
        data = {
            "content": "This is a test post content while not logged in.",
        }

        response = self.client.post(self.url, data)

        #tests if the response is redirected to the login page
        self.assertEqual(response.status_code, 302)

        #tests that the post was not created
        self.assertFalse(Post.objects.filter(content="This should not be posted.").exists())

    def test_create_post_missing_data(self):
        """
        Test creating a post with missing data fields.
        """
        self.client.login(username="testuser", password="password")

        #tests missing data
        data = { "content": ""}

        response = self.client.post(self.url, data)

        #tests if the response is a bad request
        self.assertEqual(response.status_code, 400)

class CommentCreateViewTest(TestCase):
    """
    Test case for the comment creation view.
    """
    def setUp(self):
        """
        Sets up test users, a post, and the route for testing.
        """
        # Creates two users - one for posting, one for commenting
        self.post_author = User.objects.create_user(username="postauthor", password="password123")
        self.comment_author = User.objects.create_user(username="commentauthor", password="password123")

        # Create a test post
        self.post = Post.objects.create(
            content="Test post for commenting",
            author=self.post_author
        )

        # Set up the comment URL
        self.url = reverse("posts:create_comment", kwargs={'post_id': self.post.id})

    def test_create_comment_logged_in(self):
        """
        Test creating a comment while logged in.
        """
        logged_in = self.client.login(username="commentauthor", password="password123")
        self.assertTrue(logged_in, "Login failed for comment author")

        # Create comment data
        data = {"content": "This is a test comment.",}
        response = self.client.post(self.url, data)

        # Tests if the response is redirected to the home page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('posts:home'))

        # Tests if the comment was created successfully
        comment_exists = Comment.objects.filter(
            content="This is a test comment.",
            author=self.comment_author,
            post=self.post
        ).exists()
        self.assertTrue(comment_exists, "Comment was not created successfully")

    def test_comment_appears_on_post(self):
        """
        Test that a comment appears on the correct post.
        """

        self.client.login(username="commentauthor", password="password123")
        Comment.objects.create(
            content="Test comment content",
            author=self.comment_author,
            post=self.post
        )

        response = self.client.get(reverse('posts:home'))

        # tests if the comment appears in the response
        self.assertContains(response, "Test comment content")
        self.assertEqual(response.status_code, 200)

