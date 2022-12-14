# Generated by Django 4.1.3 on 2022-11-04 23:24

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
            name='GrupoB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(default='Qatar', max_length=200, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(default='Equador', max_length=200, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(default='Senegal', max_length=200, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(default='Holanda', max_length=200, verbose_name='Seleção 4')),
                ('res1', models.SmallIntegerField(blank=True, null=True)),
                ('res2', models.SmallIntegerField(blank=True, null=True)),
                ('res3', models.SmallIntegerField(blank=True, null=True)),
                ('res4', models.SmallIntegerField(blank=True, null=True)),
                ('res5', models.SmallIntegerField(blank=True, null=True)),
                ('res6', models.SmallIntegerField(blank=True, null=True)),
                ('res7', models.SmallIntegerField(blank=True, null=True)),
                ('res8', models.SmallIntegerField(blank=True, null=True)),
                ('res9', models.SmallIntegerField(blank=True, null=True)),
                ('res10', models.SmallIntegerField(blank=True, null=True)),
                ('res11', models.SmallIntegerField(blank=True, null=True)),
                ('res12', models.SmallIntegerField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(default='Qatar', max_length=200, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(default='Equador', max_length=200, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(default='Senegal', max_length=200, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(default='Holanda', max_length=200, verbose_name='Seleção 4')),
                ('res1', models.SmallIntegerField(blank=True, null=True)),
                ('res2', models.SmallIntegerField(blank=True, null=True)),
                ('res3', models.SmallIntegerField(blank=True, null=True)),
                ('res4', models.SmallIntegerField(blank=True, null=True)),
                ('res5', models.SmallIntegerField(blank=True, null=True)),
                ('res6', models.SmallIntegerField(blank=True, null=True)),
                ('res7', models.SmallIntegerField(blank=True, null=True)),
                ('res8', models.SmallIntegerField(blank=True, null=True)),
                ('res9', models.SmallIntegerField(blank=True, null=True)),
                ('res10', models.SmallIntegerField(blank=True, null=True)),
                ('res11', models.SmallIntegerField(blank=True, null=True)),
                ('res12', models.SmallIntegerField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Grupo A',
                'verbose_name_plural': 'Grupo A',
            },
        ),
    ]
