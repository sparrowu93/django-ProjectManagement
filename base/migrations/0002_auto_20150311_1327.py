# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(help_text=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4', null=True, verbose_name='\u4efb\u52a1\u65f6\u95f4', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='plan_date',
            field=models.DateTimeField(help_text=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4', null=True, verbose_name='\u4efb\u52a1\u622a\u6b62\u65f6\u95f4', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='task_progress',
            field=models.IntegerField(default=0, help_text=b'%', max_length=2, verbose_name='\u4efb\u52a1\u8fdb\u5ea6'),
            preserve_default=True,
        ),
    ]
