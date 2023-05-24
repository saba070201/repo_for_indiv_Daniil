from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
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
             return redirect('home')
          except IntegrityError:
             return render(request,'accs/signup.html',{'form':UserCreationForm(),'error':'this is error'})
       else:
           return render(request,'accs/signup.html',{'form':UserCreationForm(),'error':'password did not match '})  
       

@login_required
def signout(request):
   if request.method=='POST':
      logout(request)
      return redirect('home')


def signin(request):
    if request.method=='GET':
      return render(request,'accs/signin.html',{'form':AuthenticationForm()})
    else:
      u=authenticate(request,username=request.POST["username"],password=request.POST["password"])
    
      if u is None:
          return render(request,'accs/signin.html',{'form':AuthenticationForm(),'error':'user is not exists'})
      else:
        login(request,u)
        return redirect('home')

