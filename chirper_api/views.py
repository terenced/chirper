from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.db.models import Q


import serializers
import models

@api_view(['POST'])
def register_user(request):
    user = models.User()
    try:
        user.username = request.DATA["username"]
        user.password = request.DATA["password"]

        if request.DATA.has_key("first_name"):
            user.first_name = request.DATA["first_name"]

        if request.DATA.has_key("last_name"):
            request.DATA["last_name"]

        user.save()
        token = Token.objects.get(user__username = user.username)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    except Exception, e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_chirp(request):
    
    try:
        user = models.User.objects.get(username = request.user)
        
        chirp = models.Chirp()
        chirp.content = request.DATA['chirp']
        chirp.user = user
        chirp.save()

        return Response('', status=status.HTTP_201_CREATED)
    except Exception, e:
        print e
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserRegistration(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    model = models.User
    serializer_class = serializers.UserRegistrationSerializer


class UserList(generics.ListCreateAPIView):
    model = models.User
    serializer_class = serializers.UserDetailsSerializer

class UserDetails(generics.RetrieveAPIView):
    model = models.User
    serializer_class = serializers.UserDetailsSerializer
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

