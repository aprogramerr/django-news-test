# Generated by Django 5.1 on 2024-08-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('dr', 'Draft'), ('pb', 'Published'), ('ar', 'Archived')], default='dr', max_length=2),
        ),
    ]
