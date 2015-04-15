# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0033_auto_20150306_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('SerialId', models.ForeignKey(to='snippets.Serial', default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('Device_type', models.CharField(blank=True, max_length=100, default='')),
                ('RegistrationId', models.CharField(blank=True, max_length=100, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subscription',
            name='UserId',
            field=models.ForeignKey(to='snippets.User', default=''),
            preserve_default=True,
        ),
    ]
