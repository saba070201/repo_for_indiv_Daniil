from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

class Tag(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class Like(models.Model):
    user=models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveBigIntegerField()
    content_object=GenericForeignKey('content_type','object_id')

class Item(models.Model):
    title=models.CharField(max_length=100)
    memo =models.TextField()
    image=models.ImageField(upload_to='newsapp/images',null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published=models.BooleanField(default=False,null=False,blank=False)
    likes=GenericRelation(Like)
    tags=models.ManyToManyField(Tag)
    class Meta:
        permissions=[('can_read_item','Can read item')]
    @property
    def total_likes(self):
        return self.likes.count()
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


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    class Meta:
        unique_together=('user','item',)

