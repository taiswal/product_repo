from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('myapp1/',index2),
    path('myapp1/home2',home2),
    path('myapp1/about2',about2)
]