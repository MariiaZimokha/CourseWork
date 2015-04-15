# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0031_auto_20150306_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='RegestrationId',
            new_name='RegistrationId',
        ),
    ]
