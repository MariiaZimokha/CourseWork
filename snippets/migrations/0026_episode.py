# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0025_auto_20150301_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=100, default='', blank=True)),
                ('Number', models.IntegerField()),
                ('DayRealease', models.DateField(auto_now_add=True)),
                ('EpisodeId', models.IntegerField()),
                ('season', models.ForeignKey(to='snippets.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
