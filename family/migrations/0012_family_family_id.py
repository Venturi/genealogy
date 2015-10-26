# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0011_remove_family_family_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='family_id',
            field=models.CharField(default=datetime.datetime(2015, 10, 20, 14, 51, 38, 897506, tzinfo=utc), max_length=24),
            preserve_default=False,
        ),
    ]
