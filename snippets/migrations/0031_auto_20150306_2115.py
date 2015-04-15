# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0030_auto_20150306_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SerialId', models.ForeignKey(default='', to='snippets.Serial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Device_type', models.CharField(max_length=100, blank=True, default='')),
                ('RegestrationId', models.CharField(max_length=100, blank=True, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subscription',
            name='UserId',
            field=models.ForeignKey(default='', to='snippets.User'),
            preserve_default=True,
        ),
    ]
