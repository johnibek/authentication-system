from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User
from users.utils import log_user_activity


class RegisterSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'password',
            'confirm_password',
            'refresh_token',
            'access_token'
        )
        extra_kwargs = {
            'username': {'write_only': True},
            'phone_number': {'write_only': True},
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise ValidationError(
                {
                    'success': False,
                    'message': 'Password and confirm password do not match.'
                }
            )

        validate_password(password)
        validate_password(confirm_password)

        return attrs

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

    def create(self, validated_data):
        request = self.context.get('request')
        username = validated_data.get('username')
        phone_number = validated_data.get('phone_number')
        password = validated_data.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            raise ValidationError('User with this credentials has already been created.')

        new_user = User.objects.create(
            username=username,
            phone_number=phone_number
        )
        new_user.set_password(password)
        new_user.save()

        log_user_activity(request, new_user, 'register')

        return new_user.tokens
