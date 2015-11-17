# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0024_auto_20151110_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_family_id',
            field=models.ForeignKey(verbose_name=b'ID Familia', to='family.Family'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_partner_id',
            field=models.IntegerField(default=0, null=True, verbose_name=b'ID Pareja', blank=True),
        ),
    ]
