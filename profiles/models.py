# First-party
from likes.models import Like

#Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


def nameFile(instance, filename):
    return '/'.join(['images', filename])

class UserProfile(models.Model):
    
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,related_name="profile")
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    likes = GenericRelation(Like)


    def __str__(self):
        return self.user.username

    @property
    def total_likes(self):
        return self.likes.count()