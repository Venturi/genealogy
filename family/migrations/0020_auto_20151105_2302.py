# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0019_auto_20151105_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_sex',
            field=models.CharField(max_length=20, verbose_name=b'Sexo', choices=[(b'Hombre', b'Hombre'), (b'Mujer', b'Mujer'), (b'No especificado', b'No especificado')]),
        ),
    ]
