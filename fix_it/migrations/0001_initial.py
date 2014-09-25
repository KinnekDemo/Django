# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(related_name=b'annotations', default=b'1', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_liked', models.BooleanField(default=False)),
                ('like_sum', models.IntegerField(default=0)),
                ('like_bool', models.ForeignKey(related_name=b'likes', to=settings.AUTH_USER_MODEL)),
                ('liked_comment', models.ForeignKey(related_name=b'likes', to='fix_it.Annotate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'img', blank=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('author', models.ForeignKey(related_name=b'posts', default=b'', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=15)),
                ('post', models.ForeignKey(related_name=b'tags', to='fix_it.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='annotate',
            name='post',
            field=models.ForeignKey(related_name=b'comments', to='fix_it.Post'),
            preserve_default=True,
        ),
    ]
