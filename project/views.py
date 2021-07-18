from project.models import PostProjects
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm,ImageForm
from django.contrib.auth import authenticate,login,logout as dj_login
from django.contrib.auth.decorators import login_required



# Create your views here.

def Home(request):
    projects=PostProjects.objects.all()
    user=request.user
    
    context= { 'projects':projects,'user':user}

    return render(request,'home.html',context)

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
            return redirect('Home')
        else:
            messages.info(request,'Username or password is incorrect')
       
    context={}
    return render(request,'login.html',context)

@login_required(login_url='loginpage')
def logout(request):
    
    return redirect('loginpage')

def uploadImage(request):
    if request.method == "POST":

        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
        return redirect('Home')
    else:
        form=ImageForm()
        img=PostProjects.objects.all()
    return render(request,"index.html",{"form":form})

def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
    
        searched_name = PostProjects.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"name": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required
def profile(request):
    return render(request, 'profile.html')