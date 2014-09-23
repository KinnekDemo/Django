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
    author = models.ForeignKey(User, related_name='annotations', default='1', blank=True, null=True)
    total_votes = models.IntegerField(default=0)
    up_votes = models.SmallIntegerField(default=0)
    down_votes = models.SmallIntegerField(default=0)
    thumb_up = models.BooleanField(default=False)
    thumb_down = models.BooleanField(default=False)

    def get_votes(self):
        total_votes = self.up_votes - self.down_votes
        return total_votes


    def __unicode__(self):
        return "{}".format(self.post)


class Tag(models.Model):
    label = models.CharField(max_length=15)
    post = models.ForeignKey(Post, related_name='tags')

    def __unicode__(self):
        return "{}".format(self.label)
