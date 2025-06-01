from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(write_only=True)

    def validate(self, attrs):
        refresh_token = attrs.get('refresh_token')
        user = self.context.get('request').user

        try:
            token = RefreshToken(refresh_token)
        except Exception as e:
            raise ValidationError(
                {
                    'success': False,
                    'message': 'Refresh token is invalid or expired.'
                }
            )

        if token.payload['user_id'] != user.id:
            raise ValidationError(
                {
                    'success': False,
                    'message': 'This refresh token does not belong to the authenticated user.'
                }
            )

        return attrs


    def create(self, validated_data):
        refresh_token = validated_data.get('refresh_token')

        token = RefreshToken(refresh_token)

        token.blacklist()

        return {
            'success': True,
            'message': 'Refresh token blacklisted successfully.'
        }

