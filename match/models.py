from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Match(models.Model):
    user = models.ForeignKey("auth.User",db_index=True,on_delete=models.CASCADE,related_name="match")
    match_status = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type","object_id")

    
    def mathed(self):
        if not self.match_status:
            self.match_status = True
