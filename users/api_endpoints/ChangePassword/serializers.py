from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=20, write_only=True, required=True)
    new_password = serializers.CharField(max_length=20, write_only=True, required=True)
    confirm_new_password = serializers.CharField(max_length=20, write_only=True, required=True)

    def validate(self, attrs):
        user = self.context.get('request').user
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_new_password = attrs.get('confirm_new_password')

        if not user.check_password(old_password):
            raise ValidationError(
                {
                    'success': False,
                    'message': 'Old password is incorrect.'
                }
            )

        if new_password == old_password:
            raise ValidationError(
                {
                    'success': False,
                    'message': 'New password is the same with old password.'
                }
            )

        if new_password != confirm_new_password:
            raise ValidationError(
                {
                    'success': False,
                    'message': 'New password and confirm password do not match.'
                }
            )


        validate_password(new_password)

        return attrs

    def update(self, instance, validated_data):
        new_password = validated_data.get('new_password')

        instance.set_password(new_password)
        instance.save()

        return instance

