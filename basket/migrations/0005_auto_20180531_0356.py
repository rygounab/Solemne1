# Generated by Django 2.0.4 on 2018-05-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_auto_20180531_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
