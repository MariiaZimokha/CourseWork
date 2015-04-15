# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0034_auto_20150306_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='serial',
            field=models.ForeignKey(to='snippets.Serial', related_name='seasons'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='RegistrationId',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
