from django.db import models
from django.contrib.auth.models import User


class Micropost(models.Model):

    content = models.CharField(max_length=160)
    author = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        return self.content
