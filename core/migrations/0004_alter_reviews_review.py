# Generated by Django 3.2.5 on 2021-08-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_reviews_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
