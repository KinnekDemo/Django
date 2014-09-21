from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', default='')

    def __unicode__(self):
        return "{}".format(self.body)


class Annotate(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')
    voted = models.IntegerField(default=0)
    up_voted = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}".format(self.post)


class Tag(models.Model):
    label = models.CharField(max_length=15)
    post = models.ForeignKey(Post, related_name='tags')

    def __unicode__(self):
        return "{}".format(self.label)
