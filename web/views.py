from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post

def post_list(request):
    me = User.objects.get(username='root')
    posts = Post.objects.filter(author=me)
    return render(request, 'web/post_list.html', {'posts': posts})