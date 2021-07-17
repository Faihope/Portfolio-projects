from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout as dj_login


# Create your views here.

def Home(request):

    return render(request,'home.html')

def RegisterUser(request):

    title = 'Register - projects'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            'title':title,
            'form':form,
                        }

    return render(request,'register.html',context)

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=  request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
       
    context={}
    return render(request,'login.html',context)