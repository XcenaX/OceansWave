# Generated by Django 3.1.7 on 2021-05-10 06:10

from django.db import migrations, models
import oceanswave.yandex_s3_storage


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210510_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.FileField(blank=True, null=True, storage=oceanswave.yandex_s3_storage.ClientDocsStorage(), upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, null=True, storage=oceanswave.yandex_s3_storage.ClientDocsStorage(), upload_to=''),
        ),
    ]
