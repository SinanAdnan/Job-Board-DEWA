# Generated by Django 4.2.7 on 2024-01-03 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_catogery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_catogery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.catogery'),
            preserve_default=False,
        ),
    ]
