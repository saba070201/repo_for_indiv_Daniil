from coreapp import views
from django.urls import path,include
app_name='coreapp'
urlpatterns = [
 path('',views.gohome,name='gohome')
     
]