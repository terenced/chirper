from rest_framework import generics
import serializers
import models


class ChirpsCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.ChirpSerializer
    queryset = models.Chirp.objects.all()
