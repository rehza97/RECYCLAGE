# Generated by Django 5.0.4 on 2024-04-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collecteur',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='vendeur',
            field=models.BooleanField(default=False),
        ),
    ]
