from django.db import models


class Micropost(models.Model):

    content = models.CharField(max_length=160)
    # author = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        return self.content


class User(models.Model):
    pseudo = models.CharField(max_length=32)
    pw_hash = models.CharField(max_length=32)
    posts = models.ForeignKey(Micropost)

    def __unicode__(self):
        return self.pseudo
