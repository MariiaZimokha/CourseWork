# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0029_auto_20150306_2113'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='User',
        ),
    ]
