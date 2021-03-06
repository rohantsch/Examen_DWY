# Generated by Django 2.1.2 on 2018-12-04 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('totalPresupuesto', models.IntegerField()),
                ('totalProductosComprados', models.IntegerField()),
                ('costoTotalPresupuesto', models.IntegerField()),
                ('costoTotalReal', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precioPresupuesto', models.IntegerField()),
                ('precioReal', models.IntegerField()),
                ('observacion', models.CharField(max_length=100)),
                ('comprado', models.BooleanField()),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_store.Lista')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('nombreSucursal', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contrasenia', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_store.Tienda'),
        ),
        migrations.AddField(
            model_name='lista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_store.Usuario'),
        ),
    ]
