from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import LoginSerializer
from users.models import User


class LoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    http_method_names = ['post']