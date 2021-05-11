# Generated by Django 3.1.7 on 2021-05-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_event_qr_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]