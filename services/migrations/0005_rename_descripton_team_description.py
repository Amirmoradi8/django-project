# Generated by Django 5.1.1 on 2024-10-12 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_team_instagram_team_telegram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='descripton',
            new_name='description',
        ),
    ]
