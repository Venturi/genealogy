# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0023_auto_20151106_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_partner_id',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
