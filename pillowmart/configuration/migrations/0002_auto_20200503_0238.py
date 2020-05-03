# Generated by Django 2.2.11 on 2020-05-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresse', models.CharField(max_length=255)),
                ('commune', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('code_postal', models.CharField(max_length=255)),
                ('innovate_message', models.TextField()),
                ('admin_message', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Temoignage',
                'verbose_name_plural': 'Temoignages',
            },
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('fa-facebook-f', 'Facebook'), ('fa-instagram', 'Instagram'), ('fa-google-plus-g', 'Google+'), ('fa-linkedin-in', 'Linkedin')], max_length=20),
        ),
    ]