# Generated by Django 5.0.3 on 2024-04-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='prix',
            new_name='price',
        ),
        migrations.AddField(
            model_name='flat',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
    ]
