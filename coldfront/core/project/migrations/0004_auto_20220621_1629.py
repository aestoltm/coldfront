# Generated by Django 3.2.13 on 2022-06-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_historicalprojectuseremail_projectuseremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprojectuseremail',
            name='bcc',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalprojectuseremail',
            name='cc',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='projectuseremail',
            name='bcc',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='projectuseremail',
            name='cc',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]