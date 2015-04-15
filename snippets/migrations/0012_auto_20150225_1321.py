# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20150225_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='season',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='SerialId',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='UserId',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
