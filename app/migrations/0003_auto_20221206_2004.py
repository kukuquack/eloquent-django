# Generated by Django 3.1.14 on 2022-12-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221206_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credits',
            field=models.IntegerField(default=0),
        ),
    ]
