import datetime

from django.db import models
from model_utils.models import TimeStampedModel
from opaque_keys.edx.django.models import CourseKeyField

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


class FormFillingDates(TimeStampedModel):
    course = models.OneToOneField(CourseOverview, db_index=True, on_delete=models.CASCADE, default='course-v1:edX+DemoX+Demo_Course')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.course.display_name

    def show_form(self):
        """
        Returns True if students are allowed to fill the form 
        otherwise returns false

        based on return value form will be displayed
        """
        if self.start_date.date() <= datetime.datetime.now().date() and self.end_date.date() >= datetime.datetime.now().date():
            return True
        else:
            return False


class StudentConsultationList(TimeStampedModel):
    course_id = CourseKeyField(max_length=255)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    contact_name = models.CharField(max_length=50)
    contact_phone_number = models.CharField(max_length=10)
    other_requirements = models.TextField(max_length=200, blank=True)
    other_comments = models.TextField(max_length=200, blank=True)
