# Generated by Django 4.1.4 on 2023-01-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertapp', '0004_rename_date_files_dt'),
    ]

    operations = [
        migrations.CreateModel(
            name='videofiles',
            fields=[
                ('req', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('fl', models.FileField(upload_to='')),
                ('otformat', models.CharField(default='.mp3', max_length=5)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]