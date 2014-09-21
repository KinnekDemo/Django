# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0011_auto_20140921_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotate',
            name='vote',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotate',
            name='vote_count',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
