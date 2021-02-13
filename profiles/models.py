from likes.models import Like
from match.models import Match

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point




def nameFile(instance, filename):
    return '/'.join(['images', filename])

class Profile(models.Model):
    
    SUB = (
    ('Basic', 'Basic'),
    ('Vip', 'Vip'),
    ('Premium', 'Premium'),
)
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,related_name="profile")
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=nameFile,blank=True,null=True)
    likes = GenericRelation(Like)
    match = GenericRelation(Match)
    subscription = models.CharField(max_length=14,choices=SUB,default='Basic')
    radius = models.PositiveIntegerField(default=25)
    swipe = models.PositiveIntegerField(blank=True,null=True)
    point = models.PointField(blank=True, null=True)

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def all_match(self):
        return self.match.all()

    def save(self,* args, **kwargs):
        
        if self.subscription == 'Basic':
            self.swipe = 20
            self.radius = 10
        elif self.subscription == 'Vip':
            self.swipe = 100
            self.radius = 25
        elif self.subscription == 'Premium':
            self.swipe = None
            self.radius = self.radius

        super(Profile, self).save(*args, **kwargs)