from django.contrib import admin
from lms.djangoapps.HandsOnPractical.models import FormFillingDate, StudentConsultationList,CoursePracticalDate


# @admin.register(FormFillingDate)
# class FormFillingDate(admin.ModelAdmin):
#     list_display = ['courseoverview', 'start_date', 'end_date']


@admin.register(StudentConsultationList)
class StudentConsultationList(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'practical_name']


class FormFillingDate(admin.StackedInline):
    model = FormFillingDate

@admin.register(CoursePracticalDate)
class CoursePracticalDate(admin.ModelAdmin):
    # list_display = ('display_name','user_email')
    save_as = True
    inlines = [FormFillingDate,] 
