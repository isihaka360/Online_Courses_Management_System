from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.conf.urls import handler404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .models import User

#edu_platform all request handlers

def _404_view(request, exception):
    return render(request, '404.html', status=404)

def _500_view(request):
    return render(request, '500.html', status=500)

def _course_enrollment(request):
    
    return render(request, 'edu_platform/authentication/enrollment.html')
    
def _registrationView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmed_password = request.POST.get('confirmed_password')

        if password == confirmed_password:
            try:
                hash_password = make_password(password)
                user = User.objects.create_user(username=username, email=email, password=hash_password, first_name=firstname, last_name=lastname)
                return redirect('login')
            except ValidationError as e:
                error_message = e.message_dict
                return render(request, 'edu_platform/authentication/registration.html', {'error_message': error_message})
        else:
            return render(request, 'edu_platform/authentication/registration.html', {'error_message': 'Passwords do not match'})
    else:
        return render(request, 'edu_platform/authentication/registration.html')

    
    

def _loginView(request):
    """_loginView function for login users of edu_platform
        The function uses login and authenticate methods to login user
        render and redirect methods used to login user """
        
    if request.method == 'POST':
            
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        # Authenticate user
        user = authenticate(request , username = username, password = password)
             
        if user is not None:
            # User authentication successful
            login(request, user)
            return redirect ('student dash')
            # return render (request , 'edu_platform/authenticate/student_dash.html')
        else:
            # Invalid email or password
            return render(request, 'edu_platform/authentication/login.html', {'error_message': 'Invalid username or password.'})
    else:
        # GET request, render login page
     return render(request, 'edu_platform/authentication/login.html')

login_required(login_url='login')
def _student_dashboardView(request):
    """The function will rendering for student dashboard and controlling all necessary info
        corresponding to student dashboard student's details"""
            # Get authenticated user's name
    user_name = request.user.username 
    first_name = request.user.first_name
    last_name = request.user.last_name
    
    # Other logic to fetch data for the dashboard

    context = {
        
        'user_name': user_name,
        'first_name':first_name,
        'last_name':last_name,
        # Other context variables for the dashboard
        
    }
    return render(request, 'edu_platform/authentication/student_dash.html' , context)
    
    
def _course_detailsView(request):
    """ _ displays detailed information about a specific course.
Shows course description, instructor details, lesson module"""
    pass
def _course_listView(request):
    """funct """
    return render(request, 'edu_platform/course_listing.html')
def _lesson_detailsView(request):
    """"""
    pass
def _exam_detailsView(request):
    pass

def _grade_exam_detailsView(request):
    pass

def _aboutView(request):
    """_aboutView function for rendering the contents about edu_platform"""
    return render(request, 'edu_platform/about.html')

@login_required
def _logoutView(request):
    """_logoutView function for logging out user from edu_platform's system dashboard login form""" 
    return redirect ('login')