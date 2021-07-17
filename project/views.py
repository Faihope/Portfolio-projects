from django.shortcuts import render

# Create your views here.

def Home(request):

    return render(request,'home.html')

def RegisterUser(request):

    return render(request,'register.html')