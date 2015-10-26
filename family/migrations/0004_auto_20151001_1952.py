# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_auto_20151001_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_profile_image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_rip',
            field=models.DateField(verbose_name=b'rip_date', blank=True),
        ),
    ]
