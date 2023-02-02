from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class LogoutAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # if self.request.data.get('all'):  # 全裝置登出
        #     for token in OutstandingToken.objects.filter(user=request.user):
        #         _, _ = BlacklistedToken.objects.get_or_create(token=token)
        #     return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK"})