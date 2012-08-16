from django.db import models


class Micropost(models.Model):
    class Meta:
        verbose_name = _('Micropost')
        verbose_name_plural = _('Microposts')

    content = models.CharField(max_length=160)
    author = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        pass

class User(models.Model):
    # TODO: Define fields here

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __unicode__(self):
        pass

    def save(self):
        pass

    @models.permalink
    def get_absolute_url(self):
        return ('')

    # TODO: Defne custom methods here
