from .models import UserActivityLog


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]

    return request.META.get('REMOTE_ADDR')


def log_user_activity(request, user, action):
    ip = get_user_ip(request)

    UserActivityLog.objects.create(
        action=action,
        user=user,
        ip_address=ip
    )
