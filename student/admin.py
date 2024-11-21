from django.contrib import admin
from .models import Parent, Student

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_contact', 'mother_contact')
    search_fields = ('father_name', 'mother_name', 'father_contact', 'mother_contact')
    list_filter = ('father_name', 'mother_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 
        'student_class', 'religion', 'joining_date', 'mobile_number', 
        'admission_number', 'section'
    )
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class', 'admission_number')  # Fixed typo
    list_filter = ('gender', 'student_class', 'section')
    readonly_fields = ('student_image',)
