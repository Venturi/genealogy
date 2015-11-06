# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0017_auto_20151105_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_birth',
            field=models.DateField(help_text=b'Fecha en este formato <em>YYYY-MM-DD</em>', verbose_name=b'Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_name',
            field=models.CharField(help_text=b'Nombre del nuevo miembro...', max_length=100, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_sex',
            field=models.CharField(help_text=b'Sexo...', max_length=20, verbose_name=b'Sexo'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_surname',
            field=models.CharField(help_text=b'Apellidos del nuevo miembro...', max_length=100, verbose_name=b'Apellidos'),
        ),
    ]
