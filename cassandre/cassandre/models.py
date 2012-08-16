from django.db import models


class Micropost(models.Model):
    class Meta:
        verbose_name = _('Micropost')
        verbose_name_plural = _('Microposts')

    content = models.CharField(max_length=160)
    author = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        return self.content
