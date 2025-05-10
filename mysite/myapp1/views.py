from django.shortcuts import render

# Create your views here.


def index2(request):
    return render(request,'index2.html')

def home2(request):
    return render(request,'home2.html')

def about2(request):
    return render(request,'about2.html')