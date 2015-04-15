# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_auto_20150225_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(blank=True, max_length=100, default='')),
                ('DayRealease', models.DateField(auto_now_add=True)),
                ('season', models.ForeignKey(to='snippets.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('SerialId', models.ForeignKey(to='snippets.Serial', default='')),
                ('UserId', models.ForeignKey(to='snippets.User', default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
