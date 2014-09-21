# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0013_auto_20140921_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='vote_count',
            new_name='down_voted',
        ),
        migrations.AddField(
            model_name='annotate',
            name='up_voted',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
