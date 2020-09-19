from django.shortcuts import render,redirect
from .models import user
from django.contrib.auth import login
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.views.generic import ListView
from django.urls import reverse

def indexPage(request):
    return render(request, 'index.html')

# Create your views here.
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    currStudent = {}
    try:
        currStudent=user.objects.get(name=username)
        details = user.objects.filter(category = 'student')
    except ObjectDoesNotExist:
        return render(request,'register.html')
    if(currStudent.password == password):
        response = render(request, 'home.html', {'currUser' : currStudent, 'allDetails': details}) 
        response.set_cookie('last_connection', datetime.datetime.now())
        response.set_cookie('username', currStudent.name)
        return response
    return render(request,'index.html')


def homePage(request):
    username = request.COOKIES['username']
    currUser = user.objects.get(name=username)
    currdetails = user.objects.filter(category = 'student')
    return render(request, 'home.html', {'currUser': currUser, 'allDetails': currdetails})

def signupPage(request):
    return render(request,'register.html')

def register(request):
    # db = student()
    # db.email = request.POST.get('email')
    # db.password = request.POST.get('password')
    # db.re_password = request.POST.get('re_password')
    # db.save()

    name = request.POST.get('username')
    email = request.POST.get('email')
    category = request.POST.get('category')
    password = request.POST.get('psw')
    re_password = request.POST.get('psw-repeat')
    if(password == re_password):
        db = user(name=name, category=category, email=email, password=password)
        db.save()
        return render(request,'index.html')
    return render(request,'register.html') 

def markPage(request):
    username = request.COOKIES['username']
    studNames = user.objects.filter(category = 'student')
    return render(request, 'mark.html', {'username': username, 'studNames': studNames})

def mark(request):
    name = request.POST.get('username')
    currUser = {}
    print(name)
    try:
       currUser = user.objects.get(name =name) 
    except ObjectDoesNotExist:
        return render(request,'mark.html')
    currUser.mark1 = request.POST.get('mark1')
    currUser.mark2 = request.POST.get('mark2')
    currUser.mark3 = request.POST.get('mark3')
    currUser.save()
    return homePage(request)
    #return render(request,'mark.html',{'currUser':currStudent})  
def logout(request):
    response = render(request,'index.html')
    response.delete_cookie('last_connection')
    response.delete_cookie('username')
    return response
