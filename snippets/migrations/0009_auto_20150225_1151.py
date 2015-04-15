# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20150225_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(default='', blank=True, max_length=100)),
                ('DayRealease', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('NumberOfSeason', models.IntegerField()),
                ('serial', models.ForeignKey(to='snippets.Serial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(to='snippets.Season'),
            preserve_default=True,
        ),
    ]
