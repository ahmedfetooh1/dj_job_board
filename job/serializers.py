from rest_framework import serializers
from .models import JOB

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JOB
        fields = '__all__'