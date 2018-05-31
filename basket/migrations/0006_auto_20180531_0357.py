# Generated by Django 2.0.4 on 2018-05-31 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20180531_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.PositiveIntegerField(help_text='Altura en cm', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.PositiveIntegerField(help_text='Peso en gramos', null=True),
        ),
    ]