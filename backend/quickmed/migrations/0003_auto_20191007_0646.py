# Generated by Django 2.2.5 on 2019-10-07 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quickmed', '0002_auto_20191007_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hospital_address',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='hospital_name',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='hospital_phone',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
