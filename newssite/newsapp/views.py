from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from newsapp import models
def home(request):
    data=models.Item.objects.all()
    return render(request,'newsapp/home.html',{'data':data})



def item(request,item_id): 
    parrentobj=get_object_or_404(models.Item,pk=item_id)
    childobject=models.SubItem.objects.all().filter(item=item_id)
    tags=parrentobj.tags.all()
    return render(request,'newsapp/item.html',{'parrentobj':parrentobj,'childobject':childobject,'tags':tags})


@login_required
def open_item_in_author_mode(request,item_id):
    item=get_object_or_404(models.Item,pk=item_id,author=request.user)
    return redirect('accs:viewitem',item_id=item_id)
# Create your views here.
