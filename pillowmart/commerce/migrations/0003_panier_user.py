# Generated by Django 2.2.11 on 2020-05-03 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0006_auto_20200503_1756'),
        ('commerce', '0002_panier'),
    ]

    operations = [
        migrations.AddField(
            model_name='panier',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_panier', to='configuration.UserAccount'),
        ),
    ]
