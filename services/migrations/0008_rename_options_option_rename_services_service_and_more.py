# Generated by Django 5.1.1 on 2024-10-30 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_category_options_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Options',
            new_name='Option',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
