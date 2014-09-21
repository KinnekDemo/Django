# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0005_auto_20140920_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='fixer',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Fixer',
        ),
    ]
