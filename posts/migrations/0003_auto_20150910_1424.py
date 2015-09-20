# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150910_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=200.0, decimal_places=2, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='order',
            field=models.ForeignKey(related_name='customerOrders', to='posts.Customer'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='customerOrder',
            field=models.ForeignKey(related_name='orderItems', to='posts.CustomerOrder'),
        ),
    ]
