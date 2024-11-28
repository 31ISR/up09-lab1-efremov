from django.shortcuts import render

def posts_lists(req):
    return render(req, 'posts/posts_list.html')

# Create your views here.
