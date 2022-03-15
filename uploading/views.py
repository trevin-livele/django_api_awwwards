from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Post




def createpost(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForm()
    return render(request, 'create_post.html', {'form': form})