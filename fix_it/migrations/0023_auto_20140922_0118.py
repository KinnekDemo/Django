# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0022_auto_20140922_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='annotate',
            old_name='post',
            new_name='posts',
        ),
    ]
