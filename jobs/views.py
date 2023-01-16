from rest_framework import viewsets
from .serializers import JobSerializer, PlatformSerializer, UserSerializer
from .models import Job, Platform
from django.contrib.auth.models import User
from rest_framework import permissions


# Create your views here.
class PlatformViewSet(viewsets.ModelViewSet):

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class JobViewSet(viewsets.ModelViewSet):
    
    queryset = Job.objects.all().order_by('-update_time')
    serializer_class = JobSerializer
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]
