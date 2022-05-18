import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import response, status, viewsets

from lms.djangoapps.course_api.views import CourseListView
from lms.djangoapps.HandsOnPractical.models import StudentConsultationList, FormFillingDate
from lms.djangoapps.HandsOnPractical.serializers import StudentConsultationListSerializer


class StudentRegistrationForm(LoginRequiredMixin, generic.TemplateView):

    """
    To display registration form
    """
    template_name = 'courseware/student_registration_form.html'

    def get_context_data(self, **kwargs):
        context = super(StudentRegistrationForm, self).get_context_data(**kwargs)
        context.update({'course_id': kwargs['course_id']})
        return context


class EventsCalendarView(LoginRequiredMixin, generic.TemplateView):
    """
    To display Full calendar js template
    """

    template_name = 'courseware/Events_details.html'


class StudentRegistrationAPI(viewsets.ModelViewSet):
    """
    def create: To check if user has entered valid data and to send mail regarding the session also
    def list: to check if user has already registered or not and return the data
    api_url : http://localhost:18000/hands-on-practical/api/student-pratical-data/
    """

    queryset = StudentConsultationList.objects.all()
    serializer_class = StudentConsultationListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # session_detais = Practical.objects.get(pk=serializer.data.get('session'))
            # template = 'emails/email.html'
            # message = render_to_string(template, {
            #     "name": session_detais.name,
            #     "start_date": session_detais.start_date,
            #     "end_date": session_detais.end_date,
            #     "description": session_detais.description
            # })

            # email = EmailMultiAlternatives('test_email', message, from_email='youremail@gmail.com', to=[serializer.data.get('email')])
            # email.attach_alternative(template, "text/html")
            # email.send()
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        user_exist_flag = False          # flag that returns true if user has already registered for the session
        
        email = request.GET.get("email")
        practical_name = request.GET.get("practical_name")

        user_exist_data = list(self.queryset.filter(email=email, practical_name=practical_name).values())

        if user_exist_data:
            user_exist_flag = True

        return response.Response({"user_exist_data": user_exist_flag})


class DisplayCoursesListAPI(viewsets.ModelViewSet):
    """
    These class returns the Course List data that needs to be displayed in Full calendar js
    Here, only necessary data is returned and in formatted manner that is understanded by Full calendar js
    api_url: http://localhost:18000/hands-on-practical/api/events-data/
    """

    def list(self, request, *args, **kwargs):
        """
        To return the Course list which is to be displayed in full calendar
        """

        all_data = FormFillingDate.objects.all()
        all_practical_list = []
        for i in all_data:
            practical_list = {}
            practical_list['title'] = i.practical_name
            practical_list['start'] = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            practical_list['end'] = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            all_practical_list.append(practical_list)

        return response.Response(all_practical_list)
