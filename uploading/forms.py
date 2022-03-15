from django import forms
from .models import Post,ReviewRating

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'image','description','post_link')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject','review','rating']