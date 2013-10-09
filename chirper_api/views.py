from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

@api_view(['POST', 'DELETE'])
def follow(request, username, followed):

    try:
        user = models.User.objects.get(username = username)
        followed = models.User.objects.get(username = followed)

    except Exception, e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        if user.id == followed.id:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        user.profile.follows.add(followed.profile)
        user.save()
        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        user.profile.follows.remove(followed.profile)
        user.save()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)




class ChirpsList(generics.ListAPIView):
    serializer_class = serializers.ChirpSerializer

    def get_queryset(self):
        user = models.User.objects.get(id=1)#self.request.user
        return models.Chirp.objects \
                          .filter(Q(user=user)| Q(user__userprofile__in=user.profile.follows.all)) \
                          .order_by('-created_on')

