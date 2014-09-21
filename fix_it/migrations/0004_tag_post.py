# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0003_auto_20140919_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(related_name=b'tags', default='', to='fix_it.Post'),
            preserve_default=False,
        ),
    ]
