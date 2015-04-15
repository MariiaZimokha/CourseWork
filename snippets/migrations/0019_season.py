# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0018_auto_20150301_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('NumberOfSeason', models.IntegerField()),
                ('SeasonId', models.IntegerField()),
                ('serialId', models.ForeignKey(to='snippets.Serial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
