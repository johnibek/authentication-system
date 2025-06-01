from django.urls import path
from users.api_endpoints import *
from .views import say_hello


urlpatterns = [
    path('hello/', say_hello, name='hello'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshAPIView.as_view(), name='login-refresh'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('change-user-info/', ChangeUserInfoAPIView.as_view(), name='change-user-info'),
]