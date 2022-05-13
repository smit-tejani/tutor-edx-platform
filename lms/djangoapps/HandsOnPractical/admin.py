from django.contrib import admin
from lms.djangoapps.HandsOnPractical.models import FormFillingDates, StudentConsultationList


@admin.register(FormFillingDates)
class FormFillingDates(admin.ModelAdmin):
    list_display = ['course', 'start_date', 'end_date']


@admin.register(StudentConsultationList)
class StudentConsultationList(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'course_id']
