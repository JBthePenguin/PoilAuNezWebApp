# Generated by Django 2.1.5 on 2019-01-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0006_auto_20190127_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='dispaly_url_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]
