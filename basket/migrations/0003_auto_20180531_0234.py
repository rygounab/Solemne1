# Generated by Django 2.0.4 on 2018-05-31 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20180424_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePartido', models.CharField(max_length=120)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='coach',
            name='dv',
        ),
        migrations.RemoveField(
            model_name='player',
            name='dv',
        ),
        migrations.RemoveField(
            model_name='team',
            name='code',
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basket.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coach',
            name='rut',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='player',
            name='rut',
            field=models.CharField(max_length=12),
        ),
        migrations.AddField(
            model_name='nomina',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.Player'),
        ),
    ]
