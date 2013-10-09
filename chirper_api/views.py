from rest_framework import generics
from django.db.models import Q

import serializers
import models


class UserList(generics.ListAPIView):
    model = models.User
    serializer_class = serializers.UserSerializer

class UserDetails(generics.RetrieveAPIView):
    model = models.User
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'


class ChirpsList(generics.ListAPIView):
    serializer_class = serializers.ChirpSerializer
    user = models.User.objects.get(id=1)
    queryset = models.Chirp.objects \
                           .filter(Q(user=user)| Q(user__userprofile__in=user.profile.follows.all)) \
                           .order_by('-created_on')


class ChirpsTimeline(generics.ListAPIView):
    serializer_class = serializers.ChirpSerializer
    queryset = models.Chirp.objects.all()
