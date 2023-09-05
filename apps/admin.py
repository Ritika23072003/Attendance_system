from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserModal(UserAdmin):
    list_display = ['username','user_type']


admin.site.register(CustomUser,UserAdmin)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)





