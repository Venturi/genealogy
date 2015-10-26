# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0012_family_family_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
