# Generated by Django 5.0.7 on 2024-08-01 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasetcreator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anotasi_dataset',
            old_name='tinngi',
            new_name='tinggi',
        ),
    ]
