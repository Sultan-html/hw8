# Generated by Django 5.1.2 on 2024-11-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegramm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]