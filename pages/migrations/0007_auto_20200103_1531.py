# Generated by Django 2.1.2 on 2020-01-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200103_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image1',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image2',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image3',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image4',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image5',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image6',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
    ]
