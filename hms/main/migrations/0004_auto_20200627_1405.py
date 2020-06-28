# Generated by Django 2.2 on 2020-06-27 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_excercise_e_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_title', models.CharField(max_length=20)),
                ('m_content', models.TextField()),
                ('m_created_at', models.DateTimeField(auto_now_add=True)),
                ('m_modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdl_title', models.CharField(max_length=20)),
                ('tdl_content', models.TextField()),
                ('tdl_created_at', models.DateTimeField(auto_now_add=True)),
                ('tdl_modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='excercise',
            name='e_description',
            field=models.TextField(),
        ),
    ]