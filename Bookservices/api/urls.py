from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ApiOverview, name='home'),
    path('create/',views.Add_Item, name='Add_Items'),
    path('all/',views.View_Items, name='View_Items'),
    path('update/<int:pk>',views.Update_Items, name='Update_Items'),
    path('item/<int:pk>/delete/',views.Delete_Item, name='Delete_Items'),
    
]