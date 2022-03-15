from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Post
from .forms import ImageForm


# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')


def login_user(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('login')



# def createpost(request):
#     if request.method == 'POST':
#         image = request.FILES.get('image')
#         description = request.POST.get('description')
#         post = Post.objects.create(user=request.user,image=image,description=description)
#         post.save()
#         return redirect('home')
#     return render(request, 'create_post.html')








def createpost(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'create_post.html', {'form': form})