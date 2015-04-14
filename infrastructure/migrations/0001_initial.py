# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=64)),
                ('port', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('uuid', models.CharField(max_length=64)),
            ],
        ),
    ]
