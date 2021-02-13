# First-party
from .models import Match
#Django
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType



User = get_user_model()

def is_vote(obj, user) -> bool:

    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    match = Match.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return match.exists()

def get_voted_persons(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        match__content_type=content_type, match__object_id=obj.id
    )
