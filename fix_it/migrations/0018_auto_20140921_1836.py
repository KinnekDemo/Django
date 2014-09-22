# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0017_auto_20140921_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='down_voted',
            new_name='thumb_down',
        ),
        migrations.RenameField(
            model_name='annotate',
            old_name='up_voted',
            new_name='thumb_up',
        ),
    ]
