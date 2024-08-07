from celery import shared_task
from .models import Rental



@shared_task
def calculate_rental_cost(rental_id):
    rental = Rental.objects.get(id=rental_id)
    duration = rental.end_time - rental.start_time
    hours = duration.total_seconds() / 3600
    rental.cost = hours * 10
    rental.save()
