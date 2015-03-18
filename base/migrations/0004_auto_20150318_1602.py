# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150311_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-status', 'priority', 'progress'], 'verbose_name': '\u9879\u76ee\u4efb\u52a1\u4fe1\u606f', 'verbose_name_plural': '\u9879\u76ee\u4efb\u52a1\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(help_text=b'issue \xe5\x86\x85\xe5\xae\xb9', max_length=100, verbose_name='\u8be6\u60c5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(help_text=b'\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', null=True, verbose_name='\u5b8c\u6210\u65e5\u671f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='plan_date',
            field=models.DateTimeField(help_text=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f', null=True, verbose_name='\u622a\u6b62\u65e5\u671f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.IntegerField(default=0, help_text=b'%', max_length=2, verbose_name='\u8fdb\u5ea6'),
            preserve_default=True,
        ),
    ]
