# Generated by Django 4.2.7 on 2023-11-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_titel'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part time'), ('Full Time', 'Full Time')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='titel',
            field=models.CharField(max_length=100),
        ),
    ]
