from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'password',
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

    def create(self, validated_data):
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

        return new_user.tokens
