# Generated by Django 3.2 on 2021-12-16 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0004_auto_20211216_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaborateur',
            old_name='id_admin',
            new_name='is_admin',
        ),
    ]
