from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import Blogpost,Contact

from django.contrib.auth.forms import  UserCreationForm
from  .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout



# Create your views here.

def index(request):
    return render(request,"index.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()	
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was Created for ' + user)
                return redirect('login')	
        context = {'form':form}
        return render(request, 'register.html',context)

    
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('blogs')
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, password=password, username=username)
			if user is not None:
				login(request,user)
				return redirect('blogs')
			else:
				messages.info(request,"Username OR Password incorrect")		
		context = {}
		return render(request,'login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('index')


def blogs(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request,"blogs.html",{'myposts': myposts})

@login_required(login_url='login')
def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blogpost.html',{'post':post})

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "contact.html")