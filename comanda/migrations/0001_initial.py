# Generated by Django 2.1 on 2018-10-06 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idusuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.Restaurante')),
            ],
        ),
        migrations.AddField(
            model_name='comanda',
            name='mesa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comanda.Mesa'),
        ),
    ]
