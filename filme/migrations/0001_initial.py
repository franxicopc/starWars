# Generated by Django 3.2.2 on 2021-05-08 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('duracao', models.CharField(max_length=10)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capa_filmes')),
                ('bilheteria', models.CharField(max_length=50)),
                ('ordem', models.IntegerField()),
                ('trailler', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=255)),
                ('filme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='filme.filme')),
            ],
        ),
    ]
