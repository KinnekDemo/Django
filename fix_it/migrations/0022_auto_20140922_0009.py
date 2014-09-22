# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0021_auto_20140922_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotate',
            name='author',
            field=models.ForeignKey(related_name=b'annotations', default=b'1', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
