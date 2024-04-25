from django.urls import path
from .views import _registrationView , _loginView , _aboutView , _logoutView , _course_listView , _course_enrollment ,_student_dashboardView

# ending points for edu_platform
urlpatterns = [
    
    path('', _aboutView , name= 'about'),
    path('register/', _registrationView , name= 'registration'),
    path('student dashboard/', _student_dashboardView , name= 'student dash'),
    path('login/', _loginView , name= 'login'),
    path('logout/', _logoutView , name = 'logout'),
    path('courses/' , _course_listView , name = 'course_list'),
    path('enrollment/' , _course_enrollment , name= 'enrollment'),
      
]
