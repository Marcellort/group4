# Generated by Django 3.1.4 on 2020-12-16 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Formularios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=250)),
                ('pergunta1', models.CharField(max_length=250)),
                ('pergunta2', models.CharField(max_length=250)),
                ('pergunta3', models.CharField(max_length=250)),
                ('pergunta4', models.CharField(max_length=250)),
                ('pergunta5', models.CharField(max_length=250)),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'eventos',
            },
        ),
    ]
