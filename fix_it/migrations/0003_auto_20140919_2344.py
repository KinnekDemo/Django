# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_it', '0002_auto_20140919_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotate',
            old_name='user_comment',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=b'img', blank=True),
        ),
    ]
