# Generated by Django 3.1 on 2020-08-25 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_todo_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complete',
            new_name='completed',
        ),
    ]
