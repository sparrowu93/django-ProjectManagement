# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150311_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_progress',
            new_name='progress',
        ),
    ]
