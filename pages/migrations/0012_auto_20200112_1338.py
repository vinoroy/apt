# Generated by Django 2.1.2 on 2020-01-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_typeservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeservice',
            old_name='name',
            new_name='serviceName',
        ),
        migrations.AddField(
            model_name='apartment',
            name='serviceName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.TypeService'),
        ),
    ]
