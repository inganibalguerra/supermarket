from rest_framework import serializers
from supermarket_ms.models.user_model import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email']
