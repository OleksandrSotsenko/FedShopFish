from rest_framework import serializers

from backend.serializers import UserSerializer
from .models import Fish


class FishSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Fish
        fields = [
            'id',
            'owner',
            'name',
            'colors',
            'life',
            'photo',
            'eating',
            'price'
        ]
