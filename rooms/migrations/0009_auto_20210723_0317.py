# Generated by Django 2.2.5 on 2021-07-22 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20210719_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bathrooms',
            new_name='baths',
        ),
    ]