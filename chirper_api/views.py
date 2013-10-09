from rest_framework import generics
from django.db.models import Q

import serializers
import models


class UserList(generics.ListAPIView):
    model = models.User
    serializer_class = serializers.UserSerializer

class ChirpsList(generics.ListAPIView):
    serializer_class = serializers.ChirpSerializer
    user = models.User.objects.get(id=2)
    queryset = models.Chirp.objects\
                           .filter(Q(user__userprofile__in=user.profile.follows.all) | Q(user=user))\
                           .order_by('-created_on')


class ChirpsTimeline(generics.ListAPIView):
    serializer_class = serializers.ChirpSerializer
    queryset = models.Chirp.objects.all()    
