# Generated by Django 3.2.7 on 2021-10-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='option',
            field=models.CharField(max_length=100),
        ),
    ]