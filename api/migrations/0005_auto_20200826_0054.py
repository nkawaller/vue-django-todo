# Generated by Django 3.1 on 2020-08-26 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200825_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='editing',
        ),
    ]
