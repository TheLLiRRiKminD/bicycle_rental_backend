from django.contrib import admin

from rentals.models import Rental, Bicycle


# Register your models here.
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time')


@admin.register(Bicycle)
class BicycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
