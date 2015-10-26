# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0005_auto_20151001_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_rip',
            field=models.DateField(verbose_name=b'rip_date', blank=True),
        ),
    ]
