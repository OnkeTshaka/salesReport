from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='productlist'),
    path('add/',views.create,name='add'),
    path('update/<str:pk>',views.edit,name='update'),
    path('delete/<str:pk>',views.remove,name='delete'),
    path('detail/<str:pk>',views.details,name='details'),
    
    
    
    ]