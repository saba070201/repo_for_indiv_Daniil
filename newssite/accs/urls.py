from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from accs.views import *
app_name='accs'
urlpatterns = [

    path('sign-up/',signup,name='signup'),
     path('sign-in/',signin,name='signin'),

    path('sign-out/',signout,name='signout'),
     
]