from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('myapp2/',index3),
    path('myapp2/home3',home3)
]