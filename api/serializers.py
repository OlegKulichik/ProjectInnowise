from match.models import Match
from profiles.models import Profile
from likes import services as likes_services
from match import services as match_services

from django.contrib.auth import get_user_model
from django.contrib.gis.geos import fromstr

from rest_framework import serializers
from generic_relations.relations import GenericRelatedField


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = (
            "id",
            "url",
            "username",
            "is_superuser"
        )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    is_fan = serializers.SerializerMethodField()
    all_match = serializers.HyperlinkedIdentityField(
        view_name="api:match-detail", many=True
    )

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "description", 
            "image", 
            "is_fan", 
            "total_likes", 
            "subscription", 
            "swipe",
            "radius",
            "point",
            "all_match",
        )
    
    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    is_vote = serializers.SerializerMethodField()
    content_object = GenericRelatedField(
        {
            Profile: serializers.HyperlinkedRelatedField(
                queryset=Profile.objects.all(), view_name="profile-detail"
            ),
            Match: serializers.HyperlinkedRelatedField(
                queryset=Match.objects.all(), view_name="match-detail"
            ),
        }
    )

    class Meta:
        model = Match
        fields = (
            "id",
            "user",
            "content_object",
            "is_vote",
        )
    
    def get_is_vote(self, obj) -> bool:
        user = self.context.get('request').user
        return match_services.is_vote(obj, user)