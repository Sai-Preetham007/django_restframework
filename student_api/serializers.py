from rest_framework import serializers
from student_api import models

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer(read_only = True)

    class Meta:
        model = models.Students
        fields = "__all__"