# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u9879\u76ee\u7684\u9636\u6bb5\u6027\u89c4\u5212', max_length=20, verbose_name='\u91cc\u7a0b\u7891')),
                ('description', models.TextField(help_text='\u5177\u4f53\u89c4\u5212', max_length=100, verbose_name='\u91cc\u7a0b\u7891\u8be6\u60c5')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u91cc\u7a0b\u7891\u4fe1\u606f',
                'verbose_name_plural': '\u9879\u76ee\u91cc\u7a0b\u7891\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u9879\u76ee\u540d')),
                ('description', models.TextField(help_text=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\x80\xe4\xbb\x8b', max_length=100, verbose_name='\u9879\u76ee\u8be6\u60c5')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u4fe1\u606f',
                'verbose_name_plural': '\u9879\u76ee\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(default=1, help_text=b'\xe7\xb1\xbb\xe5\x9e\x8b', max_length=2, verbose_name='\u7c7b\u578b', choices=[(0, b'\xe6\x97\xa0'), (1, b'Bug'), (2, b'Feature'), (3, b'Enhancement')])),
                ('status', models.IntegerField(default=0, help_text=b'\xe7\x8a\xb6\xe6\x80\x81', max_length=2, verbose_name='\u72b6\u6001', choices=[(1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (0, b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90')])),
                ('priority', models.IntegerField(default=0, help_text=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7', max_length=2, verbose_name='\u4f18\u5148\u7ea7', choices=[(0, b'\xe6\x97\xa0'), (1, b'\xe4\xbd\x8e'), (2, b'\xe4\xb8\xad'), (3, b'\xe9\xab\x98')])),
                ('name', models.CharField(help_text=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x90\x8d', max_length=20, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('description', models.TextField(help_text=b'issue \xe5\x86\x85\xe5\xae\xb9', max_length=100, verbose_name='\u4efb\u52a1\u8be6\u60c5')),
                ('created_time', models.DateTimeField(help_text=b'\xe5\x88\x9d\xe6\xac\xa1\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4', verbose_name='\u521d\u6b21\u4e0a\u4f20\u65f6\u95f4', auto_now_add=True)),
                ('updated_time', models.DateTimeField(help_text=b'\xe4\xb8\x8a\xe6\xac\xa1\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', verbose_name='\u4e0a\u6b21\u66f4\u65b0\u65f6\u95f4', auto_now=True)),
                ('assign_to', models.ForeignKey(verbose_name='\u8d1f\u8d23\u4eba', to=settings.AUTH_USER_MODEL, help_text=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe8\xb7\x9f\xe8\xbf\x9b\xe4\xba\xba')),
                ('milestone', models.ForeignKey(related_name='tasks', blank=True, to='base.Milestone', help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe9\x87\x8c\xe7\xa8\x8b\xe7\xa2\x91', null=True, verbose_name='\u6240\u5c5e\u91cc\u7a0b\u7891')),
                ('project', models.ForeignKey(related_name='tasks', verbose_name='\u6240\u5c5e\u9879\u76ee', to='base.Project', help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe9\xa1\xb9\xe7\x9b\xae')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u4efb\u52a1\u4fe1\u606f',
                'verbose_name_plural': '\u9879\u76ee\u4efb\u52a1\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(related_name='milestones', verbose_name='\u6240\u5c5e\u9879\u76ee', to='base.Project', help_text='\u6240\u5c5e\u9879\u76ee'),
            preserve_default=True,
        ),
    ]
