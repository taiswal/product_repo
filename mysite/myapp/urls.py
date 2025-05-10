from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index1),
    path('home1',home1)

]
