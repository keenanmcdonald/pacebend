# Generated by Django 3.1.1 on 2020-09-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dws', '0002_auto_20200914_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='exit_sign',
            field=models.CharField(default='', max_length=200, verbose_name='Exit Sign'),
        ),
        migrations.AlterField(
            model_name='area',
            name='picnic_table',
            field=models.IntegerField(verbose_name='Picnic Table #'),
        ),
        migrations.AlterField(
            model_name='level',
            name='routes',
            field=models.IntegerField(),
        ),
    ]
