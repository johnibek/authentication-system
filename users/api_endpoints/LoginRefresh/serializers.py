from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class LoginRefreshSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'access_token',
            'refresh_token'
        )

    def create(self, validated_data):
        refresh_token = validated_data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)

            access_token = str(token.access_token)

            return {
                'access_token': access_token
            }
        except Exception as e:
            raise ValidationError({'refresh_token': 'refresh token is invalid or expired.'})
