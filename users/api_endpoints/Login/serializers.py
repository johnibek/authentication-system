from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User
from users.utils import log_user_activity

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'access_token',
            'refresh_token'
        )


    def create(self, validated_data):
        request = self.context.get('request')
        username = validated_data.get('username')
        password = validated_data.get('password')

        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(detail="Invalid credentials.", code='user-not-found')
        if not user.check_password(password):
            raise ValidationError(detail="Invalid credentials.", code='wrong-password')

        log_user_activity(request, user, 'login')

        return user.tokens
