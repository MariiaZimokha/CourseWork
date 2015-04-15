# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0040_auto_20150412_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(default='', max_length=100, blank=True)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=100, blank=True)),
                ('Image_url', models.CharField(default='', max_length=200, blank=True)),
                ('LongDescription', models.TextField()),
                ('ShortDesctiption', models.CharField(default='', max_length=100, blank=True)),
                ('SerialId', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SerialId', models.ForeignKey(default='', to='snippets.Serial', related_name='serial')),
                ('UserId', models.ForeignKey(default='', to='snippets.User', related_name='user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='season',
            name='serial',
            field=models.ForeignKey(to='snippets.Serial', related_name='seasons'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(to='snippets.Season', related_name='episode'),
            preserve_default=True,
        ),
    ]
