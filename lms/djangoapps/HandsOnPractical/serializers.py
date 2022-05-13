from rest_framework import serializers

from lms.djangoapps.HandsOnPractical.models import FormFillingDates, StudentConsultationList


class StudentConsultationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentConsultationList
        fields = "__all__"


class FormFillingDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFillingDates
        fields = "__all__"
