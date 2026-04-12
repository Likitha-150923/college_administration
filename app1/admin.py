from django.contrib import admin

from app1.models import Student, Department, Faculty

"student"
class Student_admin(admin.ModelAdmin):
    list_display = ['stu_id','stu_name','stu_age','stu_email','stu_class','stu_marks']

admin.site.register(Student, Student_admin)

"department"
class Department_admin(admin.ModelAdmin):
    list_display = ['dept_id','dept_name','dept_code']

admin.site.register(Department, Department_admin)

"faculty"
class Faculty_admin(admin.ModelAdmin):
    list_display = ['emp_dept','emp_id','emp_name','emp_phn','emp_email','emp_date_of_join']

admin.site.register(Faculty, Faculty_admin)
# Register your models here.
