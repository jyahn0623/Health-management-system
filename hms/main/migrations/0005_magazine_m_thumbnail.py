# Generated by Django 2.2 on 2020-06-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200627_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='m_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='magazine'),
        ),
    ]
