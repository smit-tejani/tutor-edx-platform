from django.contrib import admin
from lms.djangoapps.HandsOnPractical.models import FormFillingDate, StudentConsultationList, CoursePracticalDate


@admin.register(StudentConsultationList)
class StudentConsultationList(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'practical_name']


class FormFillingDate(admin.StackedInline):
    model = FormFillingDate


@admin.register(CoursePracticalDate)
class CoursePracticalDate(admin.ModelAdmin):
    save_as = True
    inlines = [FormFillingDate, ]
