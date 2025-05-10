from django.shortcuts import render

# Create your views here.

def home1(request):
    return render(request,'home1.html')

def index1(request):
    return render(request,'index1.html')
