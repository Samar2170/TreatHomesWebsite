# Generated by Django 3.2.5 on 2021-08-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('brief', models.TextField()),
            ],
        ),
    ]