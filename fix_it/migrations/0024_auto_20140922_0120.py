# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0023_auto_20140922_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='annotate',
            old_name='posts',
            new_name='post',
        ),
    ]
