# Generated by Django 4.0.5 on 2022-06-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MascoApp', '0003_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(max_length=40, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(max_length=12, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ocupacion',
            field=models.CharField(max_length=40, verbose_name='Ocupacion'),
        ),
    ]
