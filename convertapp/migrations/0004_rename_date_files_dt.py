# Generated by Django 4.1.4 on 2023-01-26 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convertapp', '0003_rename_datetime_files_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='date',
            new_name='dt',
        ),
    ]
