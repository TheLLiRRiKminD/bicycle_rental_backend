from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('date_joined')

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
