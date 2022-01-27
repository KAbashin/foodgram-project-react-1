from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Follow

User = get_user_model()


class FollowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'