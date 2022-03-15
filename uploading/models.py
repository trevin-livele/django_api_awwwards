from django.db import models
from accounts.models import Account
from django.db import models



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