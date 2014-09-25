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
    author = models.ForeignKey(User, related_name='comments', default='1', blank=True, null=True)
    user_like = models.ForeignKey(User, related_name='comments')

    def __unicode__(self):
        return "{}".format(self.author)


class Like(models.Model):
    user_liked = models.BooleanField(default=False)
    like_sum = models.IntegerField(default=0)
    like_bool = models.ForeignKey(User, related_name='likes')
    liked_comment = models.ForeignKey(Annotate, related_name='likes')

    def __unicode__(self):
        return "{}".format(self.user)


class Tag(models.Model):
    label = models.CharField(max_length=15)
    post = models.ForeignKey(Post, related_name='tags')

    def __unicode__(self):
        return "{}".format(self.label)
