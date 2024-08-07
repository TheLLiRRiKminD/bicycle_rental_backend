from rest_framework.routers import DefaultRouter
from rentals.apps import RentalsConfig
from rentals.views import RentalViewSet, BicycleViewSet

app_name = RentalsConfig.name

router = DefaultRouter()
router.register(r'rentals', RentalViewSet, basename='Rental')
router.register(r'bicycles', BicycleViewSet, basename='Bicycle')

urlpatterns = router.urls
