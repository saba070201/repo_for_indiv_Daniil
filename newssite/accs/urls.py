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
    path('create-item/',createitem,name='createitem'),
    path('view-item-<int:item_id>/',viewitem,name='viewitem'), 
    path('change-item-<int:item_id>/',change_item,name='change_item'), 
    path('change-item-<int:item_id>/change-subitem-<int:subitem_id>/',change_subitem,name='change_subitem'),
    path('change-item-<int:item_id>/create-subitem/',create_subitem,name='create_subitem'),
    path('profile/',profile,name='profile'),
    path('publication-<int:item_id>/',publication,name='publication')
]