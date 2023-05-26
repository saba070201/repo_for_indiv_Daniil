from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from accs.forms import *
def signup(request):
    if request.method=='GET':
      return render(request,'accs/signup.html',{'form':UserCreationForm()})
    else:
       if request.POST['password1']==request.POST['password2']:
          print(str(request.POST['password1']),str(request.POST['password2']))
          try:
             user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
             user.save()
             login(request,user)
             return redirect('newsapp:home')
          except IntegrityError:
             return render(request,'accs/signup.html',{'form':UserCreationForm(),'error':'this is error'})
       else:
           return render(request,'accs/signup.html',{'form':UserCreationForm(),'error':'password did not match '})  
       

@login_required
def signout(request):
   if request.method=='POST':
      logout(request)
      return redirect('newsapp:home')


def signin(request):
    if request.method=='GET':
      return render(request,'accs/signin.html',{'form':AuthenticationForm()})
    else:
      u=authenticate(request,username=request.POST["username"],password=request.POST["password"])
    
      if u is None:
          return render(request,'accs/signin.html',{'form':AuthenticationForm(),'error':'user is not exists'})
      else:
        login(request,u)
        return redirect('newsapp:home')


@login_required
def createitem(request):
   if request.method=='GET':
      return render(request,'accs/createitem.html',{'form':CreateItemForm()})
   else: 
      try:
         form=CreateItemForm(request.POST, request.FILES)
         newitem=form.save(commit=False)
         newitem.author=request.user
         newitem.save()
         return redirect('newsapp:home')
      except ValueError:
          return render(request,'accs/createitem.html',{'form':CreateItemForm(),'error':'неккоректные данные'})
      
@login_required
def viewitem(request,item_id):
   bigitem=get_object_or_404(Item,pk=item_id,author=request.user) # над этим стоит задуматься 
   smallitems=SubItem.objects.all().filter(item=item_id)
   return render(request,'accs/viewitem.html',{'bigitem':bigitem,'smallitems':smallitems})

@login_required
def change_item(request,item_id):
   bigitem=get_object_or_404(Item,pk=item_id,author=request.user)
   if request.method=='GET':
      form=CreateItemForm(instance=bigitem)
      return render(request,'accs/change_item.html',{'form':CreateItemForm(),'bigitem':bigitem})
   else: 
      form=CreateItemForm(request.POST,request.FILES,instance=bigitem)
      form.save(commit=True)
      return redirect('newsapp:home')
