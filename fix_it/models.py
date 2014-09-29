from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', default='')
    location = models.CharField(max_length=50, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return "{}".format(self.title)


class Annotate(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(User, related_name='comments')
    like_count = models.SmallIntegerField(default=0);

    def __unicode__(self):
        return "{} on {}".format(self.author, self.post)


class Like(models.Model):
    liked = models.OneToOneField(User, related_name='likes')
    liked_comment = models.ForeignKey(Annotate, related_name='likes')

    def __unicode__(self):
        return "{}".format(self.liked)
