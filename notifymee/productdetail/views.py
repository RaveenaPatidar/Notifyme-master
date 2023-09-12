from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from .models import productdetails
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def AddnewProducts(request):
    # return render(request,'productdetail/addnewproducts.html')
    if request.method=='GET':
        if request.user.is_authenticated:
            return render(request,'productdetail/addnewproducts.html')
        else:
            return redirect('login')
    else:
        name=request.POST['product']
        url=request.POST['url']
        mail=request.POST['email']
        price=request.POST['price']
        p=productdetails(name=name,url=url,email=mail,price=price,userid_id=request.user.id)
        p.save()
        return redirect('home')
def productlist(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            id=request.user.id
            productlist=productdetails.objects.filter(userid=id)
            return render(request,'productdetail/productlist.html',{'productlist':productlist})
        else:
            return redirect('login')
