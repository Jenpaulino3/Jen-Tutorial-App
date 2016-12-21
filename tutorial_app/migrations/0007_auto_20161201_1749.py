# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial_app', '0006_auto_20161112_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='1', blank=True),
            preserve_default=False,
        ),
    ]
