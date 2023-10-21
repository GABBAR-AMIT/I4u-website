# Generated by Django 4.2.3 on 2023-09-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=20)),
                ('topic', models.CharField(max_length=20)),
                ('query', models.CharField(max_length=150)),
            ],
        ),
    ]