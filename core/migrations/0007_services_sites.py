# Generated by Django 3.2.5 on 2021-08-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ancilservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='sites',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]