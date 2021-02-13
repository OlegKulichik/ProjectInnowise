# First-party
from likes.models import Like
from match.models import Match
#Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation



def nameFile(instance, filename):
    return '/'.join(['images', filename])

class Profile(models.Model):
    
    SUB = (
    ("25swipe - 10km", 'Basic'),
    ("100 Swipe-25km", 'Vip'),
    ("no limit", 'Premium'),
)

    subscription = models.CharField(max_length=14,choices=SUB, default='Basic')
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    likes = GenericRelation(Like)
    match = GenericRelation(Match)


    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def all_match(self):
        return self.match.all()
