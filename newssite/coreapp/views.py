from django.shortcuts import render,redirect

def gohome(request):
    return redirect('newsapp:home')
# Create your views here.
