# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0003_chapter_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('leave_date', models.DateTimeField(null=True, blank=True)),
                ('chapter', models.ForeignKey(related_name='members', to='games.Chapter')),
                ('member', models.ForeignKey(related_name='chapters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='members',
        ),
    ]
