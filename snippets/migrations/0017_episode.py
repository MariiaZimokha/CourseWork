# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0016_auto_20150225_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(blank=True, default='', max_length=100)),
                ('Number', models.IntegerField()),
                ('DayRealease', models.DateField(auto_now_add=True)),
                ('season', models.ForeignKey(to='snippets.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
