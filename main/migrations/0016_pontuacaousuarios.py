# Generated by Django 4.1.3 on 2022-11-14 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0015_alter_premioindividual_artilheiro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('artilheiroGols', models.SmallIntegerField(default=0, verbose_name='Pontos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tabela Pts Usuários',
                'verbose_name_plural': 'Tabela Pts Usuários',
            },
        ),
    ]
