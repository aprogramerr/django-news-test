# Generated by Django 5.1 on 2024-09-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar/'),
        ),
    ]
