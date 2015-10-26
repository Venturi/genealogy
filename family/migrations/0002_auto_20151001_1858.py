# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='family_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='member_partner_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='member_profile_image',
            field=models.ImageField(default=datetime.datetime(2015, 10, 1, 18, 58, 23, 979956, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='member_rip',
            field=models.DateField(default=datetime.datetime(2015, 10, 1, 18, 58, 33, 415661, tzinfo=utc), verbose_name=b'rip_date'),
            preserve_default=False,
        ),
    ]
