# Generated by Django 3.1.14 on 2022-12-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20221207_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credits',
            field=models.IntegerField(default=1000),
        ),
    ]
