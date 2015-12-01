# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('family', '0025_auto_20151117_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_name', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('member_surname', models.CharField(max_length=100, verbose_name=b'Apellidos')),
                ('member_sex', models.CharField(max_length=20, verbose_name=b'Sexo', choices=[(b'Hombre', b'Hombre'), (b'Mujer', b'Mujer'), (b'No especificado', b'No especificado')])),
                ('member_birth', models.DateField(help_text=b'Fecha en este formato <em>A\xc3\x91O-MES-D\xc3\x8dA</em>', verbose_name=b'Fecha de nacimiento')),
                ('member_rip', models.DateField(null=True, verbose_name=b'Fecha de fallecimiento', blank=True)),
                ('member_profile_image', models.ImageField(upload_to=b'', null=True, verbose_name=b'Foto de perfil', blank=True)),
                ('member_partner_id', models.IntegerField(default=0, null=True, verbose_name=b'ID Pareja', blank=True)),
                ('member_email', models.EmailField(max_length=254, null=True, verbose_name=b'E-Mail', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='family',
            name='family_count',
        ),
        migrations.AlterField(
            model_name='family',
            name='family_id',
            field=models.CharField(max_length=24, verbose_name=b'ID personalizado'),
        ),
        migrations.AlterField(
            model_name='family',
            name='family_name',
            field=models.CharField(max_length=100, verbose_name=b'Apellidos familiares'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_birth',
            field=models.DateField(help_text=b'Fecha en este formato <em>A\xc3\x91O-MES-D\xc3\x8dA</em>', verbose_name=b'Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member_family_id',
            field=models.ForeignKey(verbose_name=b'ID Familia', to='family.Family'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
