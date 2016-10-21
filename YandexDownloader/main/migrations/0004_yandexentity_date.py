# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161021_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='yandexentity',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 21, 15, 9, 54, 729000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
