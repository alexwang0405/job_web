from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from jobs import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import LogoutAPIView

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout_token/', LogoutAPIView.as_view(), name='logout_token'),
    path('favor/', views.FavorAPI.as_view(), name='favor')
]
