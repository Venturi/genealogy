# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_auto_20151001_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='family_id',
            field=models.CharField(max_length=24),
        ),
    ]
