# Generated by Django 3.2.5 on 2021-08-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_reviews_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='brief',
            field=models.TextField(blank=True, null=True),
        ),
    ]
