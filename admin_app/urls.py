from django.urls import path

from admin_app.api_endpoints import *


app_name='admin_urls'
urlpatterns = [
    path('users-list/', ListUsersAPIView.as_view(), name='list-users'),
]