# Generated by Django 3.0 on 2022-12-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='имя')),
                ('number', models.IntegerField(verbose_name='число')),
                ('is_activated', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('number',),
            },
        ),
    ]
