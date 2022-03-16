from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImageForm,ReviewForm
from .models import Post,ReviewRating




def createpost(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForm()
    return render(request, 'create_post.html', {'form': form})


def submit_review(request, post_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, post__id=post_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            # messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.post_id = post_id
                data.user_id = request.user.id
                data.save()
                # messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)


def singleview(request):
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
    return render(request, 'single_view.html', context)