# Generated by Django 4.2.3 on 2023-09-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='degree',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='topic',
            field=models.CharField(max_length=50),
        ),
    ]