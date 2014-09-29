# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fix_it', '0002_auto_20140929_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liked', models.OneToOneField(related_name=b'likes', to=settings.AUTH_USER_MODEL)),
                ('liked_comment', models.ForeignKey(related_name=b'likes', to='fix_it.Annotate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='annotate',
            name='like_count',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
