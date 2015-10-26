# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0008_auto_20151001_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='family',
            new_name='member_family_id',
        ),
        migrations.RemoveField(
            model_name='family',
            name='family_id',
        ),
    ]
