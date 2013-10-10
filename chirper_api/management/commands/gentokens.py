from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(NoArgsCommand):
    help = "generate tokens for each user"

    def handle_noargs(self, **options):
        for user in User.objects.all():
            token = Token.objects.create(user=user)