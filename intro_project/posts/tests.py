from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from unittest.mock import patch, MagicMock

class PostModelTest(TestCase):
    def setUp(self):
        # Tests adding a user for posting
        self.user = User.objects.create_user(username="testuser", password="password")

    # Tests adding and saving post
    @patch('posts.models.Post.save')
    def test_add_post_mock_save(self, mock_save):
        
        post = Post.objects.create(
            title="Mock Save Test",
            content="Mock post content",
            author=self.user
        )

        #post.save()
        
        # Tests that the save method works
        mock_save.assert_called_once()


class CommentModelTest(TestCase):
    def setUp(self):
        # Tests adding a user for commenting
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(
            title="Mock comment Test",
            content="Mock post content",
            author=self.user
        )
    # Tests adding and saving comments
    @patch('posts.models.Comment.save')
    def test_add_comment_mock_save(self, mock_save):
        comment = Comment.objects.create(
            post=self.post,
            content="Mock comment content.",
            author=self.user
        )

        #comment.save()
        # Tests that the save method works
        mock_save.assert_called_once()

