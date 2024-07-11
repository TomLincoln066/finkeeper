from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import render


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)

def post_list(request):
    posts = cache.get('all_posts')
    if not posts:
        posts = Post.objects.all()
        cache.set('all_posts', posts, 60 * 15)
    return render(request, 'blog/post_list.html', {'posts': posts})