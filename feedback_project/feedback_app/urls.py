from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('feedback/',views.Feedback_View,name='feedback'),
    path('thank-you/',views.thank_you,name='thank-you')
]