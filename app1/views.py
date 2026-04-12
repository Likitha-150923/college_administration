from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app1.models import Student, Department, Faculty
from app1.forms import StudentForm, DepartmentForm, FacultyForm
from django.contrib.auth.models import User            #registration
from django.contrib.auth import login,authenticate     #login

"registration"
def clg_registration(request):
    message=''
    if request.method=="POST":
        name=request.POST.get('username')
        user_email=request.POST.get('email')
        p1=request.POST.get('password')
        p2=request.POST.get('con_password')
        if p1!=p2:
            message='password does not match Try Again'
        elif User.objects.filter(email=user_email).exists():
            message='user already exists'
        elif User.objects.filter(username=name).exists():
            message = 'Username already exists'
        else:
            new_user= User.objects.create_user(username=name,email=user_email,password=p1)
            new_user.save()
            return redirect('login')                     
    context={'message':message}
    return render(request,'registration1.html',context)                 

"login"
def clg_login(request):
    message=''
    if request.method=="POST":
        name=request.POST.get('login_username')
        p1=request.POST.get('login_password')
        user=authenticate(request,username=name,password=p1)
        if user is not None:
            login(request,user)
            message= 'User Login Successfull '
            return redirect('home')                  
        else:
            message='invalid username and password'
    context={'message':message}       
    return render(request,'login1.html',context)             


# ================= HOME =================
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


# ================= STUDENT =================

class StudentList(View):
    def get(self, request):
        data = Student.objects.all()
        return render(request, 'student_list.html', {'data': data})


class StudentCreate(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'student_form.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, 'student_form.html', {'form': form})


class StudentUpdate(View):
    def get(self, request, id):
        obj = get_object_or_404(Student, id=id)
        form = StudentForm(instance=obj)
        return render(request, 'student_form.html', {'form': form})

    def post(self, request, id):
        obj = get_object_or_404(Student, id=id)
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, 'student_form.html', {'form': form})


class StudentDelete(View):
    def get(self, request, id):
        obj = get_object_or_404(Student, id=id)
        obj.delete()
        return redirect('student_list')


# ================= DEPARTMENT =================

class DepartmentList(View):
    def get(self, request):
        data = Department.objects.all()
        return render(request, 'department_list.html', {'data': data})


class DepartmentCreate(View):
    def get(self, request):
        form = DepartmentForm()
        return render(request, 'department_form.html', {'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        return render(request, 'department_form.html', {'form': form})


class DepartmentUpdate(View):
    def get(self, request, id):
        obj = get_object_or_404(Department, id=id)
        form = DepartmentForm(instance=obj)
        return render(request, 'department_form.html', {'form': form})

    def post(self, request, id):
        obj = get_object_or_404(Department, id=id)
        form = DepartmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        return render(request, 'department_form.html', {'form': form})


class DepartmentDelete(View):
    def get(self, request, id):
        obj = get_object_or_404(Department, id=id)
        obj.delete()
        return redirect('department_list')


# ================= FACULTY =================

class FacultyList(View):
    def get(self, request):
        data = Faculty.objects.all()
        return render(request, 'faculty_list.html', {'data': data})


class FacultyCreate(View):
    def get(self, request):
        form = FacultyForm()
        return render(request, 'faculty_form.html', {'form': form})

    def post(self, request):
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
        return render(request, 'faculty_form.html', {'form': form})


class FacultyUpdate(View):
    def get(self, request, id):
        obj = get_object_or_404(Faculty, id=id)
        form = FacultyForm(instance=obj)
        return render(request, 'faculty_form.html', {'form': form})

    def post(self, request, id):
        obj = get_object_or_404(Faculty, id=id)
        form = FacultyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
        return render(request, 'faculty_form.html', {'form': form})


class FacultyDelete(View):
    def get(self, request, id):
        obj = get_object_or_404(Faculty, id=id)
        obj.delete()
        return redirect('faculty_list')