# Generated by Django 3.1.14 on 2022-12-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20221208_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credits',
            field=models.IntegerField(default=50000),
        ),
    ]