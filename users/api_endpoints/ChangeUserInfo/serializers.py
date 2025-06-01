from rest_framework import serializers

from users.models import User


class ChangeUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone_number',
            'first_name',
            'last_name',
            'email'
        )
        extra_kwargs = {
            'phone_number': {'required': False}
        }
