# Generated by Django 2.1.2 on 2020-01-26 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20200124_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='sizes',
        ),
    ]
