# Generated by Django 5.1.2 on 2024-11-03 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegramm', '0004_rename_created_telegramuser_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramuser',
            options={'verbose_name': 'польватель телеграмма', 'verbose_name_plural': 'пользователи телеграмма'},
        ),
    ]
