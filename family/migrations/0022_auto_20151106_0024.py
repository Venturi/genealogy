# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0021_auto_20151105_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_profile_image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Foto de perfil', blank=True),
        ),
    ]
