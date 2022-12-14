# Generated by Django 4.1.3 on 2022-11-07 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupob',
            options={'verbose_name': 'Grupo B', 'verbose_name_plural': 'Grupo B'},
        ),
        migrations.AlterField(
            model_name='grupoa',
            name='selecao1',
            field=models.CharField(blank=True, default='Qatar', max_length=200, null=True, verbose_name='Seleção 1'),
        ),
        migrations.AlterField(
            model_name='grupoa',
            name='selecao2',
            field=models.CharField(blank=True, default='Equador', max_length=200, null=True, verbose_name='Seleção 2'),
        ),
        migrations.AlterField(
            model_name='grupoa',
            name='selecao3',
            field=models.CharField(blank=True, default='Senegal', max_length=200, null=True, verbose_name='Seleção 3'),
        ),
        migrations.AlterField(
            model_name='grupoa',
            name='selecao4',
            field=models.CharField(blank=True, default='Holanda', max_length=200, null=True, verbose_name='Seleção 4'),
        ),
        migrations.AlterField(
            model_name='grupob',
            name='selecao1',
            field=models.CharField(blank=True, default='Inglaterra', max_length=200, null=True, verbose_name='Seleção 1'),
        ),
        migrations.AlterField(
            model_name='grupob',
            name='selecao2',
            field=models.CharField(blank=True, default='Irã', max_length=200, null=True, verbose_name='Seleção 2'),
        ),
        migrations.AlterField(
            model_name='grupob',
            name='selecao3',
            field=models.CharField(blank=True, default='Estados Unidos', max_length=200, null=True, verbose_name='Seleção 3'),
        ),
        migrations.AlterField(
            model_name='grupob',
            name='selecao4',
            field=models.CharField(blank=True, default='País de Gales', max_length=200, null=True, verbose_name='Seleção 4'),
        ),
        migrations.CreateModel(
            name='GrupoH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(blank=True, default='Portugal', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(blank=True, default='Gana', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(blank=True, default='Uruguai', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(blank=True, default='Coréia do Sul', max_length=200, null=True, verbose_name='Seleção 4')),
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
                'verbose_name': 'Grupo H',
                'verbose_name_plural': 'Grupo H',
            },
        ),
        migrations.CreateModel(
            name='GrupoG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(blank=True, default='Brasil', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(blank=True, default='Sérvia', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(blank=True, default='Suiça', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(blank=True, default='Camarões', max_length=200, null=True, verbose_name='Seleção 4')),
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
                'verbose_name': 'Grupo G',
                'verbose_name_plural': 'Grupo G',
            },
        ),
        migrations.CreateModel(
            name='GrupoF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(blank=True, default='Bélgica', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(blank=True, default='Canadá', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(blank=True, default='Marrocos', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(blank=True, default='Croácia', max_length=200, null=True, verbose_name='Seleção 4')),
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
                'verbose_name': 'Grupo F',
                'verbose_name_plural': 'Grupo F',
            },
        ),
        migrations.CreateModel(
            name='GrupoE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(blank=True, default='Espanha', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(blank=True, default='Costa Rica', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(blank=True, default='Alemanha', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(blank=True, default='Japão', max_length=200, null=True, verbose_name='Seleção 4')),
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
                'verbose_name': 'Grupo E',
                'verbose_name_plural': 'Grupo E',
            },
        ),
        migrations.CreateModel(
            name='GrupoD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(blank=True, default='França', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(blank=True, default='Austrália', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(blank=True, default='Dinamarca', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(blank=True, default='Tunísia', max_length=200, null=True, verbose_name='Seleção 4')),
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
                'verbose_name': 'Grupo D',
                'verbose_name_plural': 'Grupo D',
            },
        ),
        migrations.CreateModel(
            name='GrupoC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('selecao1', models.CharField(blank=True, default='Argentina', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2', models.CharField(blank=True, default='Arábia Saudita', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3', models.CharField(blank=True, default='México', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4', models.CharField(blank=True, default='Polônia', max_length=200, null=True, verbose_name='Seleção 4')),
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
                'verbose_name': 'Grupo C',
                'verbose_name_plural': 'Grupo C',
            },
        ),
    ]
