from rest_framework import serializers
from django.utils.timesince import timesince
import models


class UserProfileSerializer(serializers.ModelSerializer):
    follows = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.UserProfile
        fields = ('follows',)


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name', 'profile')


class ChirpSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    time_since_created = serializers.SerializerMethodField('get_time_since_created')

    class Meta:
        model = models.Chirp

    def get_time_since_created(self, obj):
        return timesince(obj.created_on)