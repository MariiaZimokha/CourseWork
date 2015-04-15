# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0037_auto_20150309_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Token',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=True,
        ),
    ]
