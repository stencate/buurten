# Generated by Django 5.1.1 on 2024-10-02 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('how_to', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='howto',
            name='hero_title',
        ),
        migrations.RemoveField(
            model_name='howto',
            name='sub_title',
        ),
    ]
