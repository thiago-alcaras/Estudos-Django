# Generated by Django 3.1.7 on 2021-03-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210318_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Laptop'), ('lni-leaf', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=17, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
    ]
