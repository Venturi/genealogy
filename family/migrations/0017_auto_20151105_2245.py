# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0016_auto_20151105_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_birth',
            field=models.DateField(verbose_name=b'Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_rip',
            field=models.DateField(null=True, verbose_name=b'Fecha de fallecimiento', blank=True),
        ),
    ]
