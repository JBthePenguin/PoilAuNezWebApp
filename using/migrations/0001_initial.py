# Generated by Django 2.1.5 on 2019-01-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/actus/')),
                ('creating_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('change_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
            ],
        ),
    ]