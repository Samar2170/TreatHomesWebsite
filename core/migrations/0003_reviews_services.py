# Generated by Django 3.2.5 on 2021-08-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_frontimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sub_head', models.CharField(max_length=250)),
                ('review', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/reviews')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('head_image', models.ImageField(blank=True, null=True, upload_to='media/service')),
                ('brief', models.TextField()),
            ],
        ),
    ]
