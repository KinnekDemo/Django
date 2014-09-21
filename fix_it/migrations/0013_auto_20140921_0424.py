# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0012_auto_20140921_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='vote',
            new_name='voted',
        ),
    ]
