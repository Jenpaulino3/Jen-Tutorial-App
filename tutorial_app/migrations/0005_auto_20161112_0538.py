# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_app', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
