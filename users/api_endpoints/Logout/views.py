from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import LogoutSerializer
from users.models import User


class LogoutAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = LogoutSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {
                'success': True,
                'message': 'Refresh token blacklisted successfully.'
            }
        )
