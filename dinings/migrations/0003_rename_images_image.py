# Generated by Django 4.1.7 on 2023-03-24 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinings', '0002_rename_links_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
