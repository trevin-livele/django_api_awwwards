from django.db import models
from accounts.models import Account



# Create your models here.
from django.db import models
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
    class Meta:
        db_table = "myapp_image"




class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    title = models.CharField(max_length=20 ,unique=True, null=True)
    description = models.CharField(max_length=200)
    date_posted  =  models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.description