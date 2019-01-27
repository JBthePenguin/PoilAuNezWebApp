# Generated by Django 2.1.5 on 2019-01-27 16:40

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0002_video_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='videos'),
        ),
    ]