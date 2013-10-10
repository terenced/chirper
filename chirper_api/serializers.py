from rest_framework import serializers
from django.utils.timesince import timesince
import models


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    follows = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.UserProfile
        fields = ('follows',)

class UserDetailsSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name', 'profile')

class ChirpSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(required=False)
    time_since_created = serializers.SerializerMethodField('get_time_since_created')

    class Meta:
        model = models.Chirp

    def get_time_since_created(self, obj):
        return timesince(obj.created_on)