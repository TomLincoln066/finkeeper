from django.test import TestCase

# Create your tests here.
from .models import Post, Tag
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        tag = Tag.objects.create(name='testtag')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        self.post.tags.add(tag)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.tags.count(), 1)

    def test_tag_uniqueness(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name='testtag')