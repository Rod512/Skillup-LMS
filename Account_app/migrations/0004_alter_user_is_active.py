# Generated by Django 5.2 on 2025-06-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_app', '0003_alter_user_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
