from django import views
from django.urls import path

from .views import *



urlpatterns = [
    path('',Homepageview.as_view(),name='home'),
    path('about/',Aboutpageview.as_view(),name='about'),
    
     
]
