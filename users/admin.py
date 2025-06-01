from django.contrib import admin
from users.models import User, UserActivityLog


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number', 'role')
    list_display_links = ('id', 'username')


@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'ip_address', 'log_time')
    list_display_links = ('id', 'user')
    ordering = ('-log_time',)
