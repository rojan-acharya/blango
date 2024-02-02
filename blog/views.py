from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Post

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  context = {
    "posts": posts
  }
  return render(request, 'blog/index.html', context)


def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  context = {
    "post": post
  }
  return render(request, "blog/post-detail.html", context)