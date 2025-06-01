from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import LoginRefreshSerializer
from users.models import User


class LoginRefreshAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = LoginRefreshSerializer
    http_method_names = ['post']
