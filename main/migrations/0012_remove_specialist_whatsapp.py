# Generated by Django 3.1.7 on 2021-05-20 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210520_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='whatsapp',
        ),
    ]
