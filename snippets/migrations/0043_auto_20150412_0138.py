# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0042_auto_20150412_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(default='', blank=True, max_length=100)),
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
                ('Name', models.CharField(default='', blank=True, max_length=100)),
                ('Image_url', models.CharField(default='', blank=True, max_length=200)),
                ('LongDescription', models.TextField()),
                ('ShortDesctiption', models.CharField(default='', blank=True, max_length=100)),
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
                ('SerialId', models.ForeignKey(default='', related_name='serial', to='snippets.Serial')),
                ('UserId', models.ForeignKey(default='', related_name='user', to='snippets.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='season',
            name='serial',
            field=models.ForeignKey(related_name='seasons', to='snippets.Serial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(related_name='episode', to='snippets.Season'),
            preserve_default=True,
        ),
    ]
