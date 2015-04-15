# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0019_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=100, blank=True, default='')),
                ('Number', models.IntegerField()),
                ('DayRealease', models.DateField(auto_now_add=True)),
                ('season', models.ForeignKey(to='snippets.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='season',
            old_name='serialId',
            new_name='serial',
        ),
    ]
