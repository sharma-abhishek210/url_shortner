# Generated by Django 4.2.5 on 2023-09-16 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortUrl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 23, 14, 40, 41, 452173, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(max_length=30, unique=True),
        ),
    ]
