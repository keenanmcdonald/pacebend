# Generated by Django 3.1.1 on 2020-09-14 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picnic_table', models.IntegerField(verbose_name='picnic table number')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_level', models.IntegerField()),
                ('routes', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dws.area')),
            ],
        ),
    ]
