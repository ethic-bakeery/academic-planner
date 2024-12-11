# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Parent', 'Parent'), ('Admin', 'Admin')],
        blank=True
    )
    profile_picture = models.URLField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended')],
        blank=True,
    )

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
    )
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    enrollment_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Graduated', 'Graduated'), ('Transferred', 'Transferred')],
        blank=True,
    )

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hire_date = models.DateField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_head = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(blank=True)
    credits = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Enrolled', 'Enrolled'), ('Completed', 'Completed'), ('Dropped', 'Dropped')],
        blank=True,
    )
    grade = models.CharField(max_length=10, blank=True)

class Classroom(models.Model):
    room_number = models.CharField(max_length=50)
    capacity = models.IntegerField(blank=True, null=True)
    building = models.CharField(max_length=255, blank=True)

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, blank=True, null=True)
    day_of_week = models.CharField(
        max_length=10,
        choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')],
        blank=True,
    )
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)
    term = models.CharField(max_length=50, blank=True)
    date_assigned = models.DateField(blank=True, null=True)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')],
        blank=True,
    )

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Overdue', 'Overdue')],
        blank=True,
    )

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    target_group = models.CharField(
        max_length=20,
        choices=[('Students', 'Students'), ('Parents', 'Parents'), ('Teachers', 'Teachers'), ('All', 'All')],
        blank=True,
    )

