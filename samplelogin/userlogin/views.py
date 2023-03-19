from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request,*args,**kwargs):
	return render(request,"home.html",{})

def signup(request,*args,**kwargs):
	if request.method =="POST":

		username=request.POST['username']
		name=request.POST['name']
		emailid=request.POST['emailid']
		password=request.POST['password']
		confirmpass=request.POST['Confirmpass']
		if password!=confirmpass:
			return redirect('signup')

		myuser=User.objects.create_user(username,emailid,password)
		myuser.name=name
		myuser.save()
		messages.success(request,"Your account has been created successfully!")

		return redirect('signin')


	return render(request,"signup.html",{})

def signin(request,*args,**kwargs):
	if request.method =='POST':
		username=request.POST['username']
		password=request.POST['password']

		user= authenticate(username=username,password=password)

		if user is not None:
			login(request,user)
			name=user.username
			return render(request,"home.html",{'name':name})
		else:
			messages.error(request,"Invalid Credentials")
			return redirect('home')




	return render(request,"signin.html",{})

def signout(request):
	logout(request)
	messages.success(request,"Logged out successfully")
	return redirect('home')