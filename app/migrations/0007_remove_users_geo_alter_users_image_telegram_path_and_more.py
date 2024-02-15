# Generated by Django 5.0.2 on 2024-02-14 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_image_path_users_image_telegram_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='geo',
        ),
        migrations.AlterField(
            model_name='users',
            name='image_telegram_path',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_premium',
            field=models.BooleanField(blank=True, editable=False, null=True, verbose_name='Премиум'),
        ),
        migrations.AlterField(
            model_name='users',
            name='language_code',
            field=models.CharField(blank=True, editable=False, max_length=2, null=True, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='users',
            name='telegram_id',
            field=models.IntegerField(editable=False, verbose_name='Телеграм ID'),
        ),
    ]