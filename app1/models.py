from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Department(models.Model):
    dept_id = models.IntegerField(unique=True)
    dept_name = models.CharField(max_length=50)
    dept_code = models.IntegerField(unique=True)
    def __str__(self):
        return self.dept_name 

class Student(models.Model):
    stu_dept = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    stu_id = models.IntegerField(unique=True)
    stu_name = models.CharField(max_length=15)
    stu_age = models.IntegerField()
    stu_email = models.EmailField()
    stu_class= models.IntegerField()
    stu_marks=models.IntegerField()

    def __str__(self):
        return self.stu_name

class Faculty(models.Model):
    emp_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=15)
    mobile = RegexValidator(
        regex=r'^[6-9]\d{9}$',
        message="Mobile must be 10 digits long"
    )
    emp_phn = models.CharField(max_length=10, validators=[mobile])
    emp_email = models.EmailField()
    emp_date_of_join = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.emp_name

# Create your models here.
