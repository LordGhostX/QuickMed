# Generated by Django 2.2.5 on 2019-12-07 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickmed', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Statistics',
        ),
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
    ]
