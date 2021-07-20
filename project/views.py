from project.models import PostProjects, Profile
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm,ImageForm,UserUpdateForm,ProfileUpdateForm
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
def logoutuser(request):
    
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
        img=Profile.objects.all()
    return render(request,"index.html",{"form":form})

def search_results(request):
    search_item=PostProjects.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        search_item=search_item.filter(name__icontains=item_name)



    # if 'name' in request.GET and request.GET["name"]:
    #     search_term = request.GET.get("name")
    
    #     searched_name = Profile.search_by_name(search_term)
    #     message = f"{search_term}"

    #     return render(request, 'search.html',{"message":message,"name": searched_name})

    # else:
    #     message = "You haven't searched for any term"
        return render(request, 'search.html')


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html',context)