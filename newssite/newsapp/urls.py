from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from newsapp import views

app_name='newsapp'
urlpatterns = [
path('',views.home,name='home'),
  path('item-<int:item_id>/',views.item,name='item'),
     
]