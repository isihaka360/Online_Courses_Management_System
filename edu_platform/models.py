from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Inherits username, first name, last name, email, and password from AbstractUser
    role_choices = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('administrator', 'Administrator'),
    )
    role = models.CharField(max_length=20, choices=role_choices)

class Course(models.Model):
    name = models.CharField(max_length=100 , null = True)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.DurationField()

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

class ExamAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

class Material(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=50)
    url = models.URLField()

class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
