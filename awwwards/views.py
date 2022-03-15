from django.shortcuts import render
from uploading.models import Post



def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'home.html', context)