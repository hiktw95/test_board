# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kkk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_title',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='board',
            name='board_content',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
