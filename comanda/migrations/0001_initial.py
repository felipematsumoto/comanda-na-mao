# Generated by Django 2.2.dev20180901131418 on 2018-11-29 11:48

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
        ('restaurante', '0001_initial'),
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('inicio', models.DateTimeField(null=True)),
                ('fim', models.DateTimeField(null=True)),
                ('pago', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=0)),
                ('coment', models.CharField(max_length=255, null=True)),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cardapio.ProdutoCardapio')),
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
        migrations.CreateModel(
            name='Cota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comanda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comanda.Comanda')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comanda.Pedido')),
            ],
        ),
        migrations.AddField(
            model_name='comanda',
            name='mesa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comanda.Mesa'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Usuario'),
        ),
    ]
