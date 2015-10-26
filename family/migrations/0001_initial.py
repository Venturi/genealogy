# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_name', models.CharField(max_length=100)),
                ('family_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_name', models.CharField(max_length=100)),
                ('member_surname', models.CharField(max_length=100)),
                ('member_sex', models.CharField(max_length=20)),
                ('member_birth', models.DateField(verbose_name=b'birth_date')),
                ('family', models.ForeignKey(to='family.Family')),
            ],
        ),
    ]
