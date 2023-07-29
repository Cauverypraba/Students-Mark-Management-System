from django.shortcuts import render, redirect
from .models import user
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from .serializers import UserSerializer

def index_page(request):
    """
    Function to main page of the application
    """
    return render(request, 'index.html')

@csrf_protect 
def login(request):
    """
    Funtion to login and enters inside student details page
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    current_student = {}
    try:
        current_student = user.objects.get(name=username)
        # Based on student category get all students details
        students_details = user.objects.filter(category = 'student')
    except ObjectDoesNotExist:
        return render(request,'register.html')
    if(current_student.password == password):
        response = render(request, 'home.html', {'current_user' : current_student, 'allDetails': students_details}) 
        response.set_cookie('last_connection', datetime.datetime.now())
        response.set_cookie('username', current_student.name)
        return response
    return redirect(signup_page)

def home_page(request):
    """
    Function to render the student details page
    """
    username = request.COOKIES['username']
    current_user = user.objects.get(name=username)
    students_details = user.objects.filter(category = 'student')
    return render(request, 'home.html', {'current_user': current_user, 'allDetails': students_details})

def signup_page(request):
    """
    Function to render the register page
    """
    return render(request,'register.html')

@api_view(['POST'])
def register(request):
    """
    Function to save user's detail in database
    """
    serializer = UserSerializer(data=request.data)
    # Checks data from request is valid and save the data
    if serializer.is_valid():
        serializer.save()
        return render(request,'index.html')
    return render(request, 'error_page.html', {'errors': serializer.errors})

def mark_page(request):
    """
    Function to just render the student mark detail page
    """
    username = request.COOKIES['username']
    students_names = user.objects.filter(category = 'student')
    return render(request, 'mark.html', {'username': username, 'students_names': students_names})

def update_mark(request):
    """
    Function to save/edit the students marks 
    """
    name = request.POST.get('username')
    current_user = {}
    try:
       current_user = user.objects.get(name =name) 
    except ObjectDoesNotExist:
        return render(request,'mark.html')
    current_user.mark1 = request.POST.get('mark1')
    current_user.mark2 = request.POST.get('mark2')
    current_user.mark3 = request.POST.get('mark3')
    current_user.save()
    return home_page(request)

def logout(request):
    """
    Function to logout from the application and delete the cookie 
    """
    response = render(request,'index.html')
    response.delete_cookie('last_connection')
    response.delete_cookie('username')
    return response

def password_reset(request):
    """
    Function to return password reset page 
    """
    return render(request, 'password_reset.html')