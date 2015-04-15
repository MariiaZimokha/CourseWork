# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0028_auto_20150304_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='FirstName',
            new_name='Device_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='UserName',
        ),
        migrations.AlterField(
            model_name='season',
            name='serial',
            field=models.ForeignKey(related_name='related_serial', to='snippets.Serial'),
            preserve_default=True,
        ),
    ]
