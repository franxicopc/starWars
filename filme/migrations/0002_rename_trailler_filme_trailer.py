# Generated by Django 3.2.2 on 2021-05-08 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='trailler',
            new_name='trailer',
        ),
    ]
