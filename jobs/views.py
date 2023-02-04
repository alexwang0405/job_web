from rest_framework import viewsets
from .serializers import JobSerializer, PlatformSerializer, UserSerializer
from .models import Job, Platform
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


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


class FavorAPI(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        
        user = User.objects.filter(id=request.user.id).first()
        favor_job = user.job_set.all()

        return Response({
            'status': 'OK',
            'data': [{
                'job_id': row.id,
                'job_name': row.job_name, 
                'job_link': row.job_link,
                } for row in favor_job],
        })

    def post(self, request):

        user = User.objects.filter(id=request.user.id).first()
        job = Job.objects.filter(id=request.data.get('job_id')).first()

        job.users.add(user)
        job.save()

        return Response({'status': 'OK'})

    def delete(self, request):

        user = User.objects.filter(id=request.user.id).first()
        job = Job.objects.filter(id=request.data.get('job_id')).first()

        job.users.remove(user)
        job.save()

        return Response({'status': 'OK'})

