# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0014_auto_20140921_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotate',
            name='down_voted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='annotate',
            name='up_voted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='annotate',
            name='voted',
            field=models.IntegerField(default=0),
        ),
    ]
