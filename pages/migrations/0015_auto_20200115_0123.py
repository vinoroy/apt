# Generated by Django 2.1.2 on 2020-01-15 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20200114_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='sizes',
            field=models.CharField(blank=True, choices=[('1', '3.5'), ('2', '4.5'), ('3', '5.5')], default='1', max_length=3, null=True),
        ),
    ]