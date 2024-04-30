# Generated by Django 5.0.4 on 2024-04-29 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collecteur', '0004_category_slug'),
        ('vendeur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poubelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poubelle_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoubelleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('poubelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendeur.poubelle')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collecteur.product')),
            ],
        ),
    ]
