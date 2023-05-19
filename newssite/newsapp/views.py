from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from newsapp import models
def home(request):
    data=models.Item.objects.all()
    return render(request,'newsapp/home.html',{'data':data})
@login_required
def item(request,item_id):
    u=request.user
    obj=get_object_or_404(models.Item,pk=item_id)
    return render(request,'newsapp/item.html',{'obj':obj,'u':u})
    
# Create your views here.
