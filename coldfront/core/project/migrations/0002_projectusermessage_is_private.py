# Generated by Django 3.2.13 on 2022-06-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectusermessage',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]