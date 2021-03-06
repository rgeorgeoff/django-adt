# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': 'comment', 'verbose_name_plural': 'comments', 'permissions': (('soft_delete_comment', 'Can soft delete comment'),)},
        ),
    ]
