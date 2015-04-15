# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0035_auto_20150308_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='SerialId',
            field=models.ForeignKey(related_name='serial', to='snippets.Serial', default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='UserId',
            field=models.ForeignKey(related_name='user', to='snippets.User', default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='RegistrationId',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
