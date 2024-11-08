from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from unittest.mock import patch, MagicMock

class PostModelTest(TestCase):
    def setUp(self):
        # Tests adding a user for posting
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(
            title="Test Creating Post",
            content="Test post content",
            author=self.user
        )

        """     # Tests adding and saving post
    @patch('posts.models.Post.save')
    def test_add_post_mock_save(self, mock_save):
        
        post = Post.objects.create(
            title="Mock Save Test",
            content="Mock post content",
            author=self.user
        ) 

        #post.save()
        
        # Tests that the save method works
        mock_save.assert_called_once() """

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Creating Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertIsInstance(self.post, Post)

class CommentModelTest(TestCase):
    def setUp(self):
        # Tests adding a user for commenting
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
        self.assertEqual(self.comment.content, "Test comment content")
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author.username, "testcommenter")
        self.assertIsInstance(self.comment, Comment)

    """# Tests adding and saving comments
    @patch('posts.models.Comment.save')
    def test_add_comment_mock_save(self, mock_save):
        comment = Comment.objects.create(
            post=self.post,
            content="Mock comment content.",
            author=self.user
        )

        #comment.save()
        # Tests that the save method works
        mock_save.assert_called_once()"""

