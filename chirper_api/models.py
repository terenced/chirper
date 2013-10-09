from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Chirp(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(default=timezone.now(), blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])