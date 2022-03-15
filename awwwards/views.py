from django.shortcuts import render
from uploading.models import Post



def home(request):
    posts = Post.objects.all()
    title = Post.objects.all()
    description = Post.objects.all()
    post_link = Post.objects.all()
    context = {
        'posts'         : posts,
        'title'         : title,
        'description'  : description,
        'post_link'     :  post_link,

    }
    return render(request, 'home.html', context)


