from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .models import User

# Course enrollment view
def _course_enrollment(request):
    return render(request, 'edu_platform/authentication/enrollment.html')

# User registration view
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

# User login view
def _loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dash')
        else:
            return render(request, 'edu_platform/authentication/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'edu_platform/authentication/login.html')

# Student dashboard view
@login_required(login_url='login')
def _student_dashboardView(request):
    user_name = request.user.username 
    first_name = request.user.first_name
    last_name = request.user.last_name
    
    # Other logic to fetch data for the dashboard

    context = {
        'user_name': user_name,
        'first_name': first_name,
        'last_name': last_name,
        # Other context variables for the dashboard
    }
    return render(request, 'edu_platform/authentication/student_dash.html', context)

# Course list view
def _course_listView(request):
    return render(request, 'edu_platform/course_listing.html')

# Other views (course details, lesson details, exam details, grade exam details) are placeholders for now
def _course_detailsView(request):
    pass

def _lesson_detailsView(request):
    pass

def _exam_detailsView(request):
    pass

def _grade_exam_detailsView(request):
    pass

# About view
def _aboutView(request):
    return render(request, 'edu_platform/about.html')

# Logout view
@login_required
def _logoutView(request):
    return redirect('login')
