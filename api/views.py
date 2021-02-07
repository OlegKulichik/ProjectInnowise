# First-party
from profiles.models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from api.mixins import LikedMixin

# Django
from django.shortcuts import render
from django.contrib.auth import get_user_model

# Third-party
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserProfileViewSet(LikedMixin, viewsets.ModelViewSet):
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)