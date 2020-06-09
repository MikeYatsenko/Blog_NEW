from django.db import models
from django.conf import settings

class Post(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog')
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='voters')

    def __str__(self):
        return self.title



class Comment(models.Model):
     creation_date = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     content = models.TextField()
     post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     comment_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_voters')

     def __str__(self):
         return self.author.username




