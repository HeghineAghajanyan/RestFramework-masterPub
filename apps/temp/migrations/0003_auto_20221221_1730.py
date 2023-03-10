# Generated by Django 3.0 on 2022-12-21 11:30

# Django
from django.db import (
    migrations,
    models
)


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_tempentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempentity',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default='2022-01-01', verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempentity',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='tempentity',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AddField(
            model_name='tempmodel',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default='2022-01-01', verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempmodel',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='tempmodel',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
    ]
