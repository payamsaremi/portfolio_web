# Generated by Django 3.2.5 on 2021-07-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagegallery',
            old_name='lead',
            new_name='post',
        ),
    ]