from django.test import TestCase
from django.contrib.auth import get_user_model
import pytest

from mixer.backend.django import mixer

from posts.models import Post

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestPostModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create sample user
        test_user1 = User.objects.create(
            username="testuser1",
            password="test123"
        )
        test_user1.save()

        # Create a sample post
        test_post = Post.objects.create(
            author=test_user1,
            title="Some title",
            body="Some body text."
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.last()
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"

        assert author == "testuser1"
        assert title == "Some title"
        assert body == "Some body text."
