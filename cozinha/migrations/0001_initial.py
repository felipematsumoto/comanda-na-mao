# Generated by Django 2.2.dev20180901131418 on 2018-10-24 20:44

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aux_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDaux', models.IntegerField()),
                ('transicao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Historico_de_Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('estado', models.IntegerField(default=0)),
                ('coment', models.CharField(max_length=255)),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cardapio.ProdutoCardapio')),
            ],
        ),
    ]
