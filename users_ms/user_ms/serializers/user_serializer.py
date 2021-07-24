from rest_framework import serializers
from user_ms.models.user_model import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user', 'password']
