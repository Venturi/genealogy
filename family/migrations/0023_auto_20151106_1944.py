# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0022_auto_20151106_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_name',
            field=models.CharField(max_length=100, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_surname',
            field=models.CharField(max_length=100, verbose_name=b'Apellidos'),
        ),
    ]
