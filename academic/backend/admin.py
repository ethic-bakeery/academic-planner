from django.contrib import admin
from .models import Profile, Student, Teacher, Department, Course, Enrollment, Classroom, Schedule, Grade, Attendance, Parent, Fee, Announcement

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'status')
    search_fields = ('user__username', 'role', 'status')
    list_filter = ('status', 'role')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'gender', 'status')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'gender')
    ordering = ('user',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'hire_date', 'specialization')
    search_fields = ('user__username', 'specialization')
    list_filter = ('hire_date',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_head')
    search_fields = ('department_name',)
    list_filter = ('department_head',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_description', 'credits', 'department', 'teacher')
    search_fields = ('course_name', 'department__department_name', 'teacher__user__username')
    list_filter = ('department', 'teacher')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'status', 'grade')
    search_fields = ('student__user__username', 'course__course_name', 'status')
    list_filter = ('status', 'course')
    ordering = ('student',)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'capacity', 'building')
    search_fields = ('room_number', 'building')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'teacher', 'classroom', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('course__course_name', 'teacher__user__username', 'classroom__room_number')
    list_filter = ('day_of_week', 'teacher', 'classroom')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'term', 'date_assigned')
    search_fields = ('student__user__username', 'course__course_name', 'term')
    list_filter = ('term',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    search_fields = ('student__user__username', 'course__course_name')
    list_filter = ('status', 'date')

class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student', 'relationship', 'phone_number')
    search_fields = ('user__username', 'student__user__username', 'relationship')

class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount_due', 'amount_paid', 'due_date', 'payment_date', 'status')
    search_fields = ('student__user__username',)
    list_filter = ('status',)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'start_date', 'end_date', 'target_group')
    search_fields = ('title', 'content', 'created_by__username')
    list_filter = ('target_group', 'start_date', 'end_date')

# Register all models
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
from django.contrib import admin

# Register your models here.
