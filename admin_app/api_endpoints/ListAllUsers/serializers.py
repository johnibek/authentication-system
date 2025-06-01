from rest_framework import serializers

from users.models import User


class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'role',
            'username',
            'phone_number',
            'first_name',
            'last_name',
            'email',
            'last_login'
        )