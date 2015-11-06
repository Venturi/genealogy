# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0020_auto_20151105_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='family_count',
            field=models.IntegerField(default=0, verbose_name=b'N\xc3\xbamero de miembros'),
        ),
        migrations.AlterField(
            model_name='family',
            name='family_name',
            field=models.CharField(max_length=100, verbose_name=b'Apellido familiar'),
        ),
    ]
