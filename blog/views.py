from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostForm, TagForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    tags = request.GET.getlist('tags')
    if query:
        posts = Post.objects.filter(tags__name__icontains=query).distinct()
    elif tags:
        posts = Post.objects.filter(tags__name__in=tags).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})