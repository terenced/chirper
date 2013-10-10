from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Chirp(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(default=timezone.now(), blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])