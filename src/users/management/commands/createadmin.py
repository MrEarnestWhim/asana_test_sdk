from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_user(
                username=settings.SUPERUSER_LOGIN,
                password=settings.SUPERUSER_PASSWORD,
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
