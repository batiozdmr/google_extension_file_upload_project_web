# Generated by Django 3.2.7 on 2022-11-03 03:29

import apps.common.fileUpload.userPath
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('slug', models.SlugField(editable=False, max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('file', models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, verbose_name='Dosya')),
                ('size', models.CharField(blank=True, max_length=200, null=True, verbose_name='Boyut')),
                ('kb_size', models.CharField(blank=True, max_length=200, null=True, verbose_name='KB Boyut')),
            ],
            options={
                'verbose_name': 'Dosyalar',
                'verbose_name_plural': 'Dosyalar',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='FileTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Dosya Tipi',
                'verbose_name_plural': 'Dosya Tipi',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TopFileTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Üst Dosya Tipi',
                'verbose_name_plural': 'Üst Dosya Tipi',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
    ]