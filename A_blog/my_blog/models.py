from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
STATUS = ((0,"Draft"),(1,"Published"))


class Post(models.Model):
    title = models.CharField(max_length=50,unique=True)
    slug = models.CharField( max_length=50,unique=True)
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home")
    