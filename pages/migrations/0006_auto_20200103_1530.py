# Generated by Django 2.1.2 on 2020-01-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200103_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='image1',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image2',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image3',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image4',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image5',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image6',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
