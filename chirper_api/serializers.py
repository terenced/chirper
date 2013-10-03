from rest_framework import serializers
import models

class ChirpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chirp