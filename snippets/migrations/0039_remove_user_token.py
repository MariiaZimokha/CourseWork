# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0038_user_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Token',
        ),
    ]
