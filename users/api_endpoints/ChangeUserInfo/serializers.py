from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class ChangeUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'first_name',
            'last_name',
            'email'
        )
        extra_kwargs = {
            'username': {'required': False},
            'phone_number': {'required': False}
        }

    def validate_username(self, username):
        if len(username) < 5 or len(username) > 30:
            raise ValidationError(
                {
                    'message': 'Your username must be 5 and 30 characters long'
                }
            )

        if username.isdigit():
            raise ValidationError(
                {
                    'message': 'Your username is entirely numeric'
                }
            )

        return username