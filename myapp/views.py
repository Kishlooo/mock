from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")

def profile(request):
    name="Kishan"
    return render(request,"myapp/profile.html",{'name':name})

def contactus(request):
    return render(request,"myapp/contactus.html")

def signin(request):
    return render(request,"myapp/signin.html")

def signup(request):
    return render(request,"myapp/signup.html")