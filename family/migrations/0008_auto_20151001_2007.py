# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0007_auto_20151001_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_rip',
            field=models.DateField(null=True, verbose_name=b'rip_date', blank=True),
        ),
    ]
