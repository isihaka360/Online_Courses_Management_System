from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} enrolled in {self.course.title} on {self.enrollment_date}"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, related_name='assignments')
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    content = models.TextField()

class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, null=True, related_name='grade')
    grade = models.FloatField()


