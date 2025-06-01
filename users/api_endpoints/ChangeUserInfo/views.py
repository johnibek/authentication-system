from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ChangeUserInfoSerializer


class ChangeUserInfoAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangeUserInfoSerializer

    def get_object(self):
        return self.request.user

