# Generated by Django 4.1.6 on 2024-07-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfert',
            name='id_abonne_destination',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='transfert',
            name='id_client_destination',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
