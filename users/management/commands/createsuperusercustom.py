import os
from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=f"{os.getenv('SU_EMAIL_ADDRESS')}",
            first_name='Admin',
            last_name='Project',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(os.getenv('SU_PASSWORD'))
        user.save()
