# Generated by Django 2.2.11 on 2020-05-03 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200503_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auteur_article', to='configuration.UserAccount'),
        ),
    ]
