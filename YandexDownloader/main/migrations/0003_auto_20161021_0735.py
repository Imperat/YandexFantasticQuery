# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161021_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yandexentity',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
