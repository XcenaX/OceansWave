# Generated by Django 3.1.7 on 2021-05-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210507_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.TextField(default=''),
        ),
    ]
