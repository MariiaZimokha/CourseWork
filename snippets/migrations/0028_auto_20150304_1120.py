# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0027_auto_20150304_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='season',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serial',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
