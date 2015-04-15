# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0044_auto_20150412_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(blank=True, default='', max_length=100)),
                ('DayRealease', models.DateField(auto_now_add=True)),
                ('EpisodeId', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NumberOfSeason', models.IntegerField()),
                ('SeasonId', models.IntegerField()),
                ('serial', models.ForeignKey(to='snippets.Serial', related_name='seasons')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(to='snippets.Season', related_name='episode'),
            preserve_default=True,
        ),
    ]
