from django.urls import path
from . import views

urlpatterns = [
    path('',views.email_view,name='sender'),
]