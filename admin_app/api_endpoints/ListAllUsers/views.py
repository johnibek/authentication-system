from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ListUsersSerializer
from users.models import User


class ListUsersAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer
    http_method_names = ['get']
