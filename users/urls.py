from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', UserViewSet, basename='User')

urlpatterns = [
                  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
              ] + router.urls
