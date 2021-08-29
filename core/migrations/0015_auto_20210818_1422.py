# Generated by Django 3.2.5 on 2021-08-18 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_phonelead_timeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('brief', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Timeline',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='brief',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='services',
            name='para',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='servicefeatures',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.services'),
        ),
    ]