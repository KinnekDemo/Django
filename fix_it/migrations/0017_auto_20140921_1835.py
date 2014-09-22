# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0016_remove_annotate_down_voted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='voted',
            new_name='total_votes',
        ),
        migrations.AddField(
            model_name='annotate',
            name='down_voted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotate',
            name='down_votes',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotate',
            name='up_votes',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
