from django.db import models
from accounts.models import Account
from django.db import models
from django.db.models import Avg


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=20 ,unique=True, null=True)
    description = models.CharField(max_length=200)
    date_posted  =  models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_link = models.CharField(max_length=20, unique=True,null=True)


    def __str__(self):
        return self.description

    def averageReview(self):
        reviews = ReviewRating.objects.filter(post=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg



class ReviewRating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,blank=True)
    review = models.TextField(max_length=500,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject