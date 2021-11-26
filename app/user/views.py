from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from app.user import serializers
from app.user.models import UserProfile


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
