# Generated by Django 3.2.3 on 2021-05-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0020_auto_20210522_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]