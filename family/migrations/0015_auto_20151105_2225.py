# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0014_auto_20151105_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_birth',
            field=models.DateField(verbose_name=b'Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_sex',
            field=models.CharField(max_length=20, verbose_name=b'Sexo'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_surname',
            field=models.CharField(max_length=100, verbose_name=b'Apellidos'),
        ),
    ]
