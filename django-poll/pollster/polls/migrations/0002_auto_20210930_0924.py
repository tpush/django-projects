# Generated by Django 3.2.7 on 2021-09-30 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Choice',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
