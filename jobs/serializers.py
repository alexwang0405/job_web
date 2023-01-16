from rest_framework import serializers
from .models import Job, Platform
from django.contrib.auth.models import User


class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
