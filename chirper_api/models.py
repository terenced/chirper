from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(pre_save, sender=User)
def populate_first_last_name(sender, instance=None, created=False, **kwargs):
    if instance.first_name == '':
        instance.first_name = "Anony"
    if instance.last_name == '':
        instance.last_name = "Mous"

class Chirp(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(default=timezone.now(), blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])