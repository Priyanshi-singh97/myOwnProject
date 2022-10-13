"""
Definition of urls for myOwnProject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app import module1 
import pract_inter
#from app.module1 import pizza 


urlpatterns = [
    
    path('contact/', views.contact, name='contact'),
    path('insert_api',module1.insert_api),
    path('search_api',module1.search_api),
    path('jf',pract_inter.fdj()),
   # path('abc',pizza().mashroom)
   
]
