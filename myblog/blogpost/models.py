from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ModelPost(models.Model):
    createdby = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.Manager()
