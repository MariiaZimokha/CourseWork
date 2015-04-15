# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0036_auto_20150308_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(to='snippets.Season', related_name='episode'),
            preserve_default=True,
        ),
    ]
