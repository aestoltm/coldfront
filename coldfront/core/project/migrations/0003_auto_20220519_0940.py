# Generated by Django 3.2.13 on 2022-05-19 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_attributetype_historicalprojectattribute_historicalprojectattributetype_projectattribute_projectattr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalprojectattribute',
            old_name='proj',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='projectattribute',
            old_name='proj',
            new_name='project',
        ),
    ]