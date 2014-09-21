# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0015_auto_20140921_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotate',
            name='down_voted',
        ),
    ]
