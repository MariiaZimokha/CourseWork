# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_auto_20150225_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(max_length=100, default='', blank=True)),
                ('DayRealease', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
