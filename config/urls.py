from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from config import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Bike Rental API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('users/', include('users.urls', namespace='users')),
                  path('', include('rentals.urls', namespace='rentals')),

                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
