from django.shortcuts import render

def helloworld(request):
    return render(request,'passwordapp/helloworld.html')
# Create your views here.
