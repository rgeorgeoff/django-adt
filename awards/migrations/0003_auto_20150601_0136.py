# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20150531_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=b'name', blank=True, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='award',
            name='type',
            field=models.ForeignKey(default=1, to='awards.AwardType'),
            preserve_default=False,
        ),
    ]
