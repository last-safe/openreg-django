# Generated by Django 5.0.2 on 2024-02-14 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_image_id_users_image_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='image_path',
            new_name='image_telegram_path',
        ),
    ]
