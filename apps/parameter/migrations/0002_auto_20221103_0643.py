# Generated by Django 3.0.8 on 2022-11-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
