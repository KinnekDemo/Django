# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fix_it', '0018_auto_20140921_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotate',
            name='author',
            field=models.ForeignKey(related_name=b'comment_authors', default='1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
