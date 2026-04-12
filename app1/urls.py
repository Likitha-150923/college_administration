from django.urls import path
from app1.views import *

urlpatterns = [

    # HOME
    path('homeview/', HomeView.as_view(), name='home'),

    # STUDENT
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/add/', StudentCreate.as_view(), name='student_create'),
    path('students/update/<int:id>/', StudentUpdate.as_view(), name='student_update'),
    path('students/delete/<int:id>/', StudentDelete.as_view(), name='student_delete'),

    # DEPARTMENT
    path('departments/', DepartmentList.as_view(), name='department_list'),
    path('departments/add/', DepartmentCreate.as_view(), name='department_create'),
    path('departments/update/<int:id>/', DepartmentUpdate.as_view(), name='department_update'),
    path('departments/delete/<int:id>/', DepartmentDelete.as_view(), name='department_delete'),

    # FACULTY
    path('faculty/', FacultyList.as_view(), name='faculty_list'),
    path('faculty/add/', FacultyCreate.as_view(), name='faculty_create'),
    path('faculty/update/<int:id>/', FacultyUpdate.as_view(), name='faculty_update'),
    path('faculty/delete/<int:id>/', FacultyDelete.as_view(), name='faculty_delete'),
]