from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.utils import log_user_activity


class LoginRefreshSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(write_only=True)
    new_refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'access_token',
            'refresh_token',
            'new_refresh_token'
        )

    def create(self, validated_data):
        request = self.context.get('request')
        refresh_token = validated_data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            user_id = token.payload.get('user_id')
            user = User.objects.get(id=user_id)

            new_token = RefreshToken.for_user(user)

            access_token = str(token.access_token)
            new_refresh_token = str(new_token)

            log_user_activity(request, user, 'login_refresh')

            return {
                'access_token': access_token,
                'new_refresh_token': new_refresh_token
            }
        except Exception as e:
            raise ValidationError({'refresh_token': 'refresh token is invalid or expired.'})
