# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_product_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('team1Score', models.IntegerField(default=1)),
                ('team2Score', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('coach', models.CharField(max_length=30)),
                ('divisionName', models.CharField(max_length=30)),
                ('league', models.ForeignKey(to='posts.League')),
            ],
        ),
        migrations.RenameField(
            model_name='customerorder',
            old_name='order',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(to='posts.League'),
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(to='posts.Location'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(related_name='team1', to='posts.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(related_name='team2', to='posts.Team'),
        ),
    ]
