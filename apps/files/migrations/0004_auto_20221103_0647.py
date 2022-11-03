# Generated by Django 3.0.8 on 2022-11-03 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0003_auto_20221103_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='files_user', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
