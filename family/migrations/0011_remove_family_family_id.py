# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0010_family_family_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='family_id',
        ),
    ]
