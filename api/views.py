from profiles.models import Profile
from match.models import Match
from .serializers import UserSerializer, ProfileSerializer, MatchSerializer
from api.mixins import LikedMixin, MatchMixin

from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfilesViewSet(MatchMixin,LikedMixin, viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MatchViewSet(viewsets.ModelViewSet):
    
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)