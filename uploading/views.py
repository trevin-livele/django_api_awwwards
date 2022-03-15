from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Post



def createpost(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST.get('description')
        post = Post.objects.create(user=request.user,image=image,description=description)
        post.save()
        return redirect('home')
    return render(request, 'create_post.html')











def createpost(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            post = form.instance
            return render(request, 'home.html', {'form': form, 'post': post})
    else:
        form = ImageForm()
    return render(request, 'create_post.html', {'form': form})