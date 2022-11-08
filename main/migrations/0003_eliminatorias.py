# Generated by Django 4.1.3 on 2022-11-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_grupob_options_alter_grupoa_selecao1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eliminatorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('primeiroA', models.CharField(choices=[('Qu', 'Qatar'), ('Eq', 'Equador'), ('Ho', 'Holanda'), ('Se', 'Senegal')], default='Qu', max_length=2)),
                ('segundoB', models.CharField(choices=[('Eu', 'Estados Unidos'), ('Pg', 'País de Gales'), ('In', 'Inglaterra'), ('Ir', 'Irâ')], default='Pg', max_length=2)),
                ('primeiroC', models.CharField(choices=[('Ar', 'Argentina'), ('As', 'Arábia Saudita'), ('Me', 'México'), ('Po', 'Polônia')], default='Ar', max_length=2)),
                ('segundoD', models.CharField(choices=[('Di', 'Dinamarca'), ('Tu', 'Tunísia'), ('Fr', 'França'), ('Au', 'Austrália')], default='Di', max_length=2)),
                ('primeiroB', models.CharField(choices=[('In', 'Inglaterra'), ('Ir', 'Irâ'), ('Eu', 'Estados Unidos'), ('Pg', 'País de Gales')], default='In', max_length=2)),
                ('segundoA', models.CharField(choices=[('Eq', 'Equador'), ('Qu', 'Qatar'), ('Ho', 'Holanda'), ('Se', 'Senegal')], default='Eq', max_length=2)),
                ('primeiroD', models.CharField(choices=[('Fr', 'França'), ('Au', 'Austrália'), ('Di', 'Dinamarca'), ('Tu', 'Tunísia')], default='Fr', max_length=2)),
                ('segundoC', models.CharField(choices=[('Ar', 'Argentina'), ('As', 'Arábia Saudita'), ('Me', 'México'), ('Po', 'Polônia')], default='Me', max_length=2)),
                ('primeiroE', models.CharField(choices=[('Al', 'Alemanha'), ('Ja', 'Japão'), ('Es', 'Espanha'), ('Cr', 'Costa Rica')], default='Al', max_length=2)),
                ('segundoF', models.CharField(choices=[('Be', 'Bélgica'), ('Ca', 'Canadá'), ('Ma', 'Marrocos'), ('Cr', 'Croácia')], default='Ma', max_length=2)),
                ('primeiroG', models.CharField(choices=[('Br', 'Brasl'), ('Se', 'Sérvia'), ('Su', 'Suiça'), ('Ca', 'Camarões')], default='Br', max_length=2)),
                ('segundoH', models.CharField(choices=[('Ur', 'Uruguai'), ('Co', 'Coréia do Sul'), ('Po', 'Portugal'), ('Ga', 'Gana')], default='Ur', max_length=2)),
                ('primeiroF', models.CharField(choices=[('Be', 'Bélgica'), ('Ca', 'Canadá'), ('Ma', 'Marrocos'), ('Cr', 'Croácia')], default='Be', max_length=2)),
                ('segundoE', models.CharField(choices=[('Al', 'Alemanha'), ('Ja', 'Japão'), ('Es', 'Espanha'), ('Cr', 'Costa Rica')], default='Es', max_length=2)),
                ('primeiroH', models.CharField(choices=[('Ur', 'Uruguai'), ('Co', 'Coréia do Sul'), ('Po', 'Portugal'), ('Ga', 'Gana')], default='Po', max_length=2)),
                ('segundoG', models.CharField(choices=[('Br', 'Brasl'), ('Se', 'Sérvia'), ('Su', 'Suiça'), ('Ca', 'Camarões')], default='Se', max_length=2)),
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
                ('res13', models.SmallIntegerField(blank=True, null=True)),
                ('res14', models.SmallIntegerField(blank=True, null=True)),
                ('res15', models.SmallIntegerField(blank=True, null=True)),
                ('res16', models.SmallIntegerField(blank=True, null=True)),
                ('selecao1Quartas', models.CharField(blank=True, default='Vencedor Jogo 49', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2Quartas', models.CharField(blank=True, default='Vencedor Jogo 50', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3Quartas', models.CharField(blank=True, default='Vencedor Jogo 51', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4Quartas', models.CharField(blank=True, default='Vencedor Jogo 52', max_length=200, null=True, verbose_name='Seleção 4')),
                ('selecao5Quartas', models.CharField(blank=True, default='Vencedor Jogo 53', max_length=200, null=True, verbose_name='Seleção 5')),
                ('selecao6Quartas', models.CharField(blank=True, default='Vencedor Jogo 54', max_length=200, null=True, verbose_name='Seleção 6')),
                ('selecao7Quartas', models.CharField(blank=True, default='Vencedor Jogo 55', max_length=200, null=True, verbose_name='Seleção 7')),
                ('selecao8Quartas', models.CharField(blank=True, default='Vencedor Jogo 56', max_length=200, null=True, verbose_name='Seleção 8')),
                ('res17', models.SmallIntegerField(blank=True, null=True)),
                ('res18', models.SmallIntegerField(blank=True, null=True)),
                ('res19', models.SmallIntegerField(blank=True, null=True)),
                ('res20', models.SmallIntegerField(blank=True, null=True)),
                ('res21', models.SmallIntegerField(blank=True, null=True)),
                ('res22', models.SmallIntegerField(blank=True, null=True)),
                ('res23', models.SmallIntegerField(blank=True, null=True)),
                ('res24', models.SmallIntegerField(blank=True, null=True)),
                ('selecao1Semi', models.CharField(blank=True, default='Vencedor Jogo 57', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2Semi', models.CharField(blank=True, default='Vencedor Jogo 58', max_length=200, null=True, verbose_name='Seleção 2')),
                ('selecao3Semi', models.CharField(blank=True, default='Vencedor Jogo 59', max_length=200, null=True, verbose_name='Seleção 3')),
                ('selecao4Semi', models.CharField(blank=True, default='Vencedor Jogo 60', max_length=200, null=True, verbose_name='Seleção 4')),
                ('res25', models.SmallIntegerField(blank=True, null=True)),
                ('res26', models.SmallIntegerField(blank=True, null=True)),
                ('res27', models.SmallIntegerField(blank=True, null=True)),
                ('res28', models.SmallIntegerField(blank=True, null=True)),
                ('selecao1TerceiroLugar', models.CharField(blank=True, default='Perdedor Jogo 61', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2TerceiroLugar', models.CharField(blank=True, default='Perdedor Jogo 62', max_length=200, null=True, verbose_name='Seleção 2')),
                ('res29', models.SmallIntegerField(blank=True, null=True)),
                ('res30', models.SmallIntegerField(blank=True, null=True)),
                ('selecao1Final', models.CharField(blank=True, default='Vencedor Jogo 61', max_length=200, null=True, verbose_name='Seleção 1')),
                ('selecao2Final', models.CharField(blank=True, default='Vencedor Jogo 62', max_length=200, null=True, verbose_name='Seleção 2')),
                ('res31', models.SmallIntegerField(blank=True, null=True)),
                ('res32', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
