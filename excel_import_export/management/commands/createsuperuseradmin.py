from django.conf import settings
from django.core.management.base import BaseCommand 
from django.contrib.auth import get_user_model 


class Command(BaseCommand): 
    help = "Create a superuser with a specified username and password"

    username = settings.SUPERUSER_USERNAME 
    password = settings.SUPERUSER_PASSWORD 
    email = settings.SUPERUSER_EMAIL 

    def handle(self, *args, **options): 
        User = get_user_model() 
        if User.objects.filter(username=self.username).exists():
            self.stdout.write(self.style.WARNING(f"User '{self.username}' already exists."))
        else:
            User.objects.create_superuser(
                username=self.username,
                password=self.password,
                email=self.email,
            )
            self.stdout.write(self.style.SUCCESS(f"Superuser '{self.username}' created successfully.")) 

