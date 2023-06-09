from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from newsapp import models
def home(request):
    user_filter_status=request.session.get('user_filter_status','down')
    
    data=models.Item.objects.all()
    if request.GET.get('filter_by')=='up':
           request.session['user_filter_status']='up'
           user_filter_status= request.session['user_filter_status']
           data=models.Item.objects.all().order_by('date')
        
    elif request.GET.get('filter_by')=='down':
            request.session['user_filter_status']='down'
            user_filter_status= request.session['user_filter_status']
            data=models.Item.objects.all().order_by('-date')
           
    return render(request,'newsapp/home.html',{'data':data,'user_filter_status':user_filter_status})


# на этом примере будут permissions 
def item(request,item_id): 
    if request.user.has_perm('newsapp.can_read_item'):
        parrentobj=get_object_or_404(models.Item,pk=item_id)
        childobject=models.SubItem.objects.all().filter(item=item_id)
        try:
            r=models.Review.objects.create(item=parrentobj,user=request.user)
            r.save()
        except:
            pass
        countofviews=models.Review.objects.filter(item=parrentobj).all().count()
        tags=parrentobj.tags.all()
        return render(request,'newsapp/item.html',{'parrentobj':parrentobj,'childobject':childobject,'tags':tags,'countofviews':countofviews})
    else:
         return HttpResponse('<h2>Permissions denied </h2>')


@login_required
def open_item_in_author_mode(request,item_id):
    item=get_object_or_404(models.Item,pk=item_id,author=request.user)
    return redirect('accs:viewitem',item_id=item_id)
# Create your views here.
