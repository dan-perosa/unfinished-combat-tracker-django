# Generated by Django 5.0.7 on 2024-07-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_battles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Battles',
            new_name='Battle',
        ),
    ]