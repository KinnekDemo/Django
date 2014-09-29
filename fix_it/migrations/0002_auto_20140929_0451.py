# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like_bool',
        ),
        migrations.RemoveField(
            model_name='like',
            name='liked_comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='annotate',
            name='author',
            field=models.ForeignKey(related_name=b'comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
