from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth,User
from django.contrib import messages
def home(request):
    return render(request,'home/home.html')

# def login(request):
#     return render(request,'home/login.html')
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
    else:
        fm = AuthenticationForm()
    return render(request,"home/login.html",{'form':fm})

# def register(request):
#     return render(request,'home/register.html')
def register(request):
        if request.method == 'GET':
            return render(request, 'home/register.html')
        else:
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
            elif password != confirm_password:
                messages.error(request, "Passwords do not match.")
            else:
                # Create a new user and set the password
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
