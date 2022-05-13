

from posixpath import basename
from django.urls import include, path, re_path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from lms.djangoapps.HandsOnPractical import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('student-pratical-data',
                views.StudentRegistrationAPI, basename='student_pratical_api'),

router.register('events-data',
                views.DisplayCoursesListAPI, basename="events_data"),

urlpatterns = []
urlpatterns += [
    re_path(r'^api/', include(router.urls)),
    re_path(r'^{}/registration-form'.format(settings.COURSE_ID_PATTERN,), views.StudentRegistrationForm.as_view(), name='practical_registration_form'),
    re_path(r'^events-calendar', views.EventsCalendarView.as_view(), name='event_calendar'),
]
