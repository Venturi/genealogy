# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0015_auto_20151105_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_birth',
            field=models.DateField(verbose_name=b'birth_date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'E-Mail', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_profile_image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Foto', blank=True),
        ),
    ]
