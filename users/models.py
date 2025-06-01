from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    USER_ROLES = (
        ('user', 'user'),
        ('manager', 'manager'),
        ('admin', 'admin')
    )

    role = models.CharField(max_length=15, choices=USER_ROLES, default='user')
    phone_number = PhoneNumberField()

    EMAIL_FIELD = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        return {
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        }

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username


class UserActivityLog(models.Model):
    ACTION_CHOICES = (
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('register', 'Register'),
        ('login_refresh', 'Login Refresh')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    ip_address = models.GenericIPAddressField()
    log_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'UserActivityLog'
        verbose_name_plural = 'UserActivityLogs'

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.log_time}"


