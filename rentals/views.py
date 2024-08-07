from datetime import timezone, datetime
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Bicycle, Rental
from .serializers import BicycleSerializer, RentalSerializer
from .tasks import calculate_rental_cost


class BicycleViewSet(viewsets.ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer

    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update']:
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    @action(detail=True, methods=['post'])
    def rent(self, request, pk=None):
        bicycle = self.get_object()

        # Проверка, что велосипед уже арендован
        if bicycle.status == 'rented':
            return Response({'error': 'Bicycle is already rented'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка, что пользователь уже имеет активную аренду
        if Rental.objects.filter(user=request.user, end_time__isnull=True).exists():
            return Response({'error': 'User already has an active rental'}, status=status.HTTP_400_BAD_REQUEST)

        # Создание новой аренды
        rental = Rental.objects.create(user=request.user, bicycle=bicycle)
        bicycle.status = 'rented'
        bicycle.save()

        return Response({'status': 'Bicycle rented', 'rental_id': rental.id}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def return_bike(self, request, pk=None):
        bicycle = self.get_object()

        # Поиск активной аренды для данного пользователя и велосипеда
        rental = Rental.objects.filter(user=request.user, bicycle=bicycle, end_time__isnull=True).first()
        if not rental:
            return Response({'error': 'No active rental found for this bicycle'}, status=status.HTTP_400_BAD_REQUEST)

        # Завершение аренды
        rental.end_time = datetime.now(timezone.utc)
        rental.save()
        bicycle.status = 'available'
        bicycle.save()

        # Асинхронный расчет стоимости аренды
        calculate_rental_cost.delay(rental.id)

        return Response({'status': 'Bicycle returned'}, status=status.HTTP_200_OK)


class RentalViewSet(viewsets.ModelViewSet):
    serializer_class = RentalSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rental.objects.filter(user=self.request.user)
