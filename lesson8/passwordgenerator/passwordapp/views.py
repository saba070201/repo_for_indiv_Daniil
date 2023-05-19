from django.shortcuts import render,HttpResponse
import random
def home(request):
    charters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('special'):
        charters+=list('!@#$%^&*()_+')
    lenght=int(request.GET.get('lenght',5))
    thepassword=''
    for i in range(lenght):
        thepassword+=random.choice(charters)
    return render(request,'passwordapp/home.html',{'thepassword':thepassword})

    