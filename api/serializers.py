# First-party
from profiles.models import UserProfile
# Django
from django.contrib.auth import get_user_model

# Third-party
from rest_framework import serializers
from generic_relations.relations import GenericRelatedField


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ("id", "url", "username", "is_superuser")

class UserProfileSerializer(serializers.ModelSerializer):
    
    is_fan = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("id","user","description", "image", "is_fan", "total_likes")

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)