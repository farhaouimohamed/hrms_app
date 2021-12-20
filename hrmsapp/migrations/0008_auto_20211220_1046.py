# Generated by Django 3.2 on 2021-12-20 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0007_mail_absence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='collaborateur',
        ),
        migrations.AddField(
            model_name='mail',
            name='email_destination',
            field=models.EmailField(default="", max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mail',
            name='email_source',
            field=models.EmailField(default="", max_length=254),
            preserve_default=False,
        ),
    ]