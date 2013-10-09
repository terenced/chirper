from rest_framework import serializers
import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name')        

class ChirpSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = models.Chirp