# Generated by Django 4.1.3 on 2022-11-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_eliminatorias_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroA',
            field=models.CharField(choices=[('Qatar', 'Qatar'), ('Equador', 'Equador'), ('Holanda', 'Holanda'), ('Senegal', 'Senegal')], default='Qatar', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroB',
            field=models.CharField(choices=[('Inglaterra', 'Inglaterra'), ('Irã', 'Irâ'), ('Estados Unidos', 'Estados Unidos'), ('País de Gales', 'País de Gales')], default='Inglaterra', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroC',
            field=models.CharField(choices=[('Argentina', 'Argentina'), ('Arábia Saudita', 'Arábia Saudita'), ('México', 'México'), ('Polônia', 'Polônia')], default='Argentina', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroD',
            field=models.CharField(choices=[('França', 'França'), ('Austrália', 'Austrália'), ('Dinamarca', 'Dinamarca'), ('Tunísia', 'Tunísia')], default='França', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroE',
            field=models.CharField(choices=[('Alemanha', 'Alemanha'), ('Japão', 'Japão'), ('Espanha', 'Espanha'), ('Costa Rica', 'Costa Rica')], default='Alemanha', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroF',
            field=models.CharField(choices=[('Bélgica', 'Bélgica'), ('Canadá', 'Canadá'), ('Marrocos', 'Marrocos'), ('Croácia', 'Croácia')], default='Bélgica', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroG',
            field=models.CharField(choices=[('Brasil', 'Brasl'), ('Sérvia', 'Sérvia'), ('Suiça', 'Suiça'), ('Camarões', 'Camarões')], default='Brasil', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='primeiroH',
            field=models.CharField(choices=[('Uruguai', 'Uruguai'), ('Coréia do Sul', 'Coréia do Sul'), ('Portugal', 'Portugal'), ('Gana', 'Gana')], default='Portugal', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoA',
            field=models.CharField(choices=[('Equador', 'Equador'), ('Qatar', 'Qatar'), ('Holanda', 'Holanda'), ('Senegal', 'Senegal')], default='Equador', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoC',
            field=models.CharField(choices=[('Argentina', 'Argentina'), ('Arábia Saudita', 'Arábia Saudita'), ('México', 'México'), ('Polônia', 'Polônia')], default='México', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoD',
            field=models.CharField(choices=[('Dinamarca', 'Dinamarca'), ('Tunísia', 'Tunísia'), ('França', 'França'), ('Austrália', 'Austrália')], default='Dinamarca', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoE',
            field=models.CharField(choices=[('Alemanha', 'Alemanha'), ('Japão', 'Japão'), ('Espanha', 'Espanha'), ('Costa Rica', 'Costa Rica')], default='Espanha', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoF',
            field=models.CharField(choices=[('Bélgica', 'Bélgica'), ('Canadá', 'Canadá'), ('Marrocos', 'Marrocos'), ('Croácia', 'Croácia')], default='Marrocos', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoG',
            field=models.CharField(choices=[('Brasil', 'Brasl'), ('Sérvia', 'Sérvia'), ('Suiça', 'Suiça'), ('Camarões', 'Camarões')], default='Sérvia', max_length=20),
        ),
        migrations.AlterField(
            model_name='eliminatorias',
            name='segundoH',
            field=models.CharField(choices=[('Uruguai', 'Uruguai'), ('Coréia do Sul', 'Coréia do Sul'), ('Portugal', 'Portugal'), ('Gana', 'Gana')], default='Uruguai', max_length=20),
        ),
    ]
