from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name='index'),
    path('home1',views.home1,name='home'),
    path('productview/home1',views.home2),
    path('your_desti',views.your_desti,name='your_desti'),
    path('productview/<int:myid>',views.productView,name='productview'),
    path('contact',views.contact,name='contact'),
    
   
]