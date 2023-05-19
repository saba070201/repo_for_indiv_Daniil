from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title=models.CharField(max_length=100)
    memo =models.TextField()
    image=models.ImageField(upload_to='newsapp/images')
    url=models.URLField(blank=True)
    date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title +'%with id%'+str(self.id)
# Create your models here.
