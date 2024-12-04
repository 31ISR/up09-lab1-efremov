from django.shortcuts import render
from .models import Post
def posts_list(req):
    posts = Post.objects.all().order_by('-date')
    return render(req, 'posts/posts_list.html', {'posts': posts}) 

# Create your views here.
