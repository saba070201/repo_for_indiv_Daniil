from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title=models.CharField(max_length=100)
    memo =models.TextField()
    image=models.ImageField(upload_to='newsapp/images',null=True,blank=True)

    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published=models.BooleanField(default=False,null=False,blank=False)
    def __str__(self) :
        return self.title +'%with id%'+str(self.id)
    
class SubItem(models.Model):
    title=models.CharField(max_length=100)
    memo =models.TextField()
    image=models.ImageField(upload_to='newsapp/images',null=True,blank=True)
    video=models.FileField(upload_to='newsapp/videos',null=True,blank=True)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    def __str__(self) :
          return self.title +'%with parrent id%'+str(self.item) 
# Create your models here.
