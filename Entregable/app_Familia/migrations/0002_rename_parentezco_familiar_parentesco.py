# Generated by Django 4.0.6 on 2022-07-18 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Familia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='parentezco',
            new_name='parentesco',
        ),
    ]
