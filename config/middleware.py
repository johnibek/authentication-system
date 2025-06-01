from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication


class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.path_role_map = {
            '/admin-user/': ['admin'],
            '/users/': ['user', 'admin', 'manager']
        }
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        try:
            user_auth_tuple = self.jwt_auth.authenticate(request)  # (user, validated_token)
            if user_auth_tuple is not None:
                request.user, _ = user_auth_tuple
        except Exception:
            pass

        if not request.user or not request.user.is_authenticated:  # Skip unauthenticated users
            return self.get_response(request)

        for path_prefix, required_roles in self.path_role_map.items():
            if request.path.startswith(path_prefix):
                print(request.path, request.user)
                user_role = getattr(request.user, 'role', None)
                if user_role not in required_roles:
                    return JsonResponse(
                        {
                            'message': 'Permission denied. You do not have access to this resource.'
                        }, status=403
                    )

        return self.get_response(request)