from django.contrib import admin
from .models import User, Course, Exam, Enrollment, ExamAttempt, Grade, Material, Announcement

# Register you
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Enrollment)
admin.site.register(ExamAttempt)
admin.site.register(Grade)
admin.site.register(Material)
admin.site.register(Announcement)




