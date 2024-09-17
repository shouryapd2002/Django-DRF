from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='Blog'),
    path('post/<str:pk>',views.post,name='Post'),
]
