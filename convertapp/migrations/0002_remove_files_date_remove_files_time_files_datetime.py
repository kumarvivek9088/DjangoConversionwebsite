# Generated by Django 4.1.4 on 2023-01-26 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('convertapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='date',
        ),
        migrations.RemoveField(
            model_name='files',
            name='time',
        ),
        migrations.AddField(
            model_name='files',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
