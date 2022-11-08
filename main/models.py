from django.contrib.auth.models import User
from django.db import models


class Base(models.Model):
    criados = models.DateField(verbose_name='Criação', auto_now_add=True)
    modificado = models.DateField(verbose_name='Atualização', auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        abstract = True
    

class GrupoA(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Qatar', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Equador', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Senegal', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Holanda', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo A'
        verbose_name_plural = 'Grupo A'

    def __str__(self):
        return f'Grupo A'
    
    
class GrupoB(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Inglaterra', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Irã', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Estados Unidos', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='País de Gales', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo B'
        verbose_name_plural = 'Grupo B'

    def __str__(self):
        return f'Grupo B'
    

class GrupoC(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Argentina', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Arábia Saudita', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='México', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Polônia', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo C'
        verbose_name_plural = 'Grupo C'

    def __str__(self):
        return f'Grupo C'
    
    
class GrupoD(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='França', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Austrália', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Dinamarca', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Tunísia', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo D'
        verbose_name_plural = 'Grupo D'

    def __str__(self):
        return f'Grupo D'
    

class GrupoE(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Espanha', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Costa Rica', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Alemanha', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Japão', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo E'
        verbose_name_plural = 'Grupo E'

    def __str__(self):
        return f'Grupo E'
    
    
class GrupoF(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Bélgica', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Canadá', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Marrocos', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Croácia', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo F'
        verbose_name_plural = 'Grupo F'

    def __str__(self):
        return f'Grupo F'


class GrupoG(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Brasil', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Sérvia', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Suiça', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Camarões', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo G'
        verbose_name_plural = 'Grupo G'

    def __str__(self):
        return f'Grupo G'


class GrupoH(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Portugal', blank=True, null=True)
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Gana', blank=True, null=True)
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Uruguai', blank=True, null=True)
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Coréia do Sul', blank=True, null=True)
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo H'
        verbose_name_plural = 'Grupo H'

    def __str__(self):
        return f'Grupo H'


class Eliminatorias(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    primeiroA = models.CharField(
        default='Qu',
        max_length=2,
        choices=(
            ('Qu', 'Qatar'),
            ('Eq', 'Equador'),
            ('Ho', 'Holanda'),
            ('Se', 'Senegal'),
        )
    )
    segundoB = models.CharField(
        default='Pg',
        max_length=2,
        choices=(
            ('Eu', 'Estados Unidos'),
            ('Pg', 'País de Gales'),
            ('In', 'Inglaterra'),
            ('Ir', 'Irâ'),
        )
    )
    primeiroC = models.CharField(
        default='Ar',
        max_length=2,
        choices=(
            ('Ar', 'Argentina'),
            ('As', 'Arábia Saudita'),
            ('Me', 'México'),
            ('Po', 'Polônia'),
        )
    )
    segundoD = models.CharField(
        default='Di',
        max_length=2,
        choices=(
            ('Di', 'Dinamarca'),
            ('Tu', 'Tunísia'),
            ('Fr', 'França'),
            ('Au', 'Austrália'),
        )
    )
    primeiroB = models.CharField(
        default='In',
        max_length=2,
        choices=(
            ('In', 'Inglaterra'),
            ('Ir', 'Irâ'),
            ('Eu', 'Estados Unidos'),
            ('Pg', 'País de Gales'),
        )
    )
    segundoA = models.CharField(
        default='Eq',
        max_length=2,
        choices=(
            ('Eq', 'Equador'),
            ('Qu', 'Qatar'),
            ('Ho', 'Holanda'),
            ('Se', 'Senegal'),
        )
    )
    primeiroD = models.CharField(
        default='Fr',
        max_length=2,
        choices=(
            ('Fr', 'França'),
            ('Au', 'Austrália'),
            ('Di', 'Dinamarca'),
            ('Tu', 'Tunísia'),
        )
    )
    segundoC = models.CharField(
        default='Me',
        max_length=2,
        choices=(
            ('Ar', 'Argentina'),
            ('As', 'Arábia Saudita'),
            ('Me', 'México'),
            ('Po', 'Polônia'),
        )
    )
    primeiroE = models.CharField(
        default='Al',
        max_length=2,
        choices=(
            ('Al', 'Alemanha'),
            ('Ja', 'Japão'),
            ('Es', 'Espanha'),
            ('Cr', 'Costa Rica'),
        )
    )
    segundoF = models.CharField(
        default='Ma',
        max_length=2,
        choices=(
            ('Be', 'Bélgica'),
            ('Ca', 'Canadá'),
            ('Ma', 'Marrocos'),
            ('Cr', 'Croácia'),
        )
    )
    primeiroG = models.CharField(
        default='Br',
        max_length=2,
        choices=(
            ('Br', 'Brasl'),
            ('Se', 'Sérvia'),
            ('Su', 'Suiça'),
            ('Ca', 'Camarões'),
        )
    )
    segundoH = models.CharField(
        default='Ur',
        max_length=2,
        choices=(
            ('Ur', 'Uruguai'),
            ('Co', 'Coréia do Sul'),
            ('Po', 'Portugal'),
            ('Ga', 'Gana'),
        )
    )
    primeiroF = models.CharField(
        default='Be',
        max_length=2,
        choices=(
            ('Be', 'Bélgica'),
            ('Ca', 'Canadá'),
            ('Ma', 'Marrocos'),
            ('Cr', 'Croácia'),
        )
    )
    segundoE = models.CharField(
        default='Es',
        max_length=2,
        choices=(
            ('Al', 'Alemanha'),
            ('Ja', 'Japão'),
            ('Es', 'Espanha'),
            ('Cr', 'Costa Rica'),
        )
    )
    primeiroH = models.CharField(
        default='Po',
        max_length=2,
        choices=(
            ('Ur', 'Uruguai'),
            ('Co', 'Coréia do Sul'),
            ('Po', 'Portugal'),
            ('Ga', 'Gana'),
        )
    )
    segundoG = models.CharField(
        default='Se',
        max_length=2,
        choices=(
            ('Br', 'Brasl'),
            ('Se', 'Sérvia'),
            ('Su', 'Suiça'),
            ('Ca', 'Camarões'),
        )
    )
    res1 = models.SmallIntegerField(blank=True, null=True)
    res2 = models.SmallIntegerField(blank=True, null=True)
    res3 = models.SmallIntegerField(blank=True, null=True)
    res4 = models.SmallIntegerField(blank=True, null=True)
    res5 = models.SmallIntegerField(blank=True, null=True)
    res6 = models.SmallIntegerField(blank=True, null=True)
    res7 = models.SmallIntegerField(blank=True, null=True)
    res8 = models.SmallIntegerField(blank=True, null=True)
    res9 = models.SmallIntegerField(blank=True, null=True)
    res10 = models.SmallIntegerField(blank=True, null=True)
    res11 = models.SmallIntegerField(blank=True, null=True)
    res12 = models.SmallIntegerField(blank=True, null=True)
    res13 = models.SmallIntegerField(blank=True, null=True)
    res14 = models.SmallIntegerField(blank=True, null=True)
    res15 = models.SmallIntegerField(blank=True, null=True)
    res16 = models.SmallIntegerField(blank=True, null=True)
    
    selecao1Quartas = models.CharField(max_length=200, verbose_name='Seleção 1', default='Vencedor Jogo 49', blank=True, null=True)
    selecao2Quartas = models.CharField(max_length=200, verbose_name='Seleção 2', default='Vencedor Jogo 50', blank=True, null=True)
    selecao3Quartas = models.CharField(max_length=200, verbose_name='Seleção 3', default='Vencedor Jogo 51', blank=True, null=True)
    selecao4Quartas = models.CharField(max_length=200, verbose_name='Seleção 4', default='Vencedor Jogo 52', blank=True, null=True)
    selecao5Quartas = models.CharField(max_length=200, verbose_name='Seleção 5', default='Vencedor Jogo 53', blank=True, null=True)
    selecao6Quartas = models.CharField(max_length=200, verbose_name='Seleção 6', default='Vencedor Jogo 54', blank=True, null=True)
    selecao7Quartas = models.CharField(max_length=200, verbose_name='Seleção 7', default='Vencedor Jogo 55', blank=True, null=True)
    selecao8Quartas = models.CharField(max_length=200, verbose_name='Seleção 8', default='Vencedor Jogo 56', blank=True, null=True)
    res17 = models.SmallIntegerField(blank=True, null=True)
    res18 = models.SmallIntegerField(blank=True, null=True)
    res19 = models.SmallIntegerField(blank=True, null=True)
    res20 = models.SmallIntegerField(blank=True, null=True)
    res21 = models.SmallIntegerField(blank=True, null=True)
    res22 = models.SmallIntegerField(blank=True, null=True)
    res23 = models.SmallIntegerField(blank=True, null=True)
    res24 = models.SmallIntegerField(blank=True, null=True)
    
    selecao1Semi = models.CharField(max_length=200, verbose_name='Seleção 1', default='Vencedor Jogo 57', blank=True, null=True)
    selecao2Semi = models.CharField(max_length=200, verbose_name='Seleção 2', default='Vencedor Jogo 58', blank=True, null=True)
    selecao3Semi = models.CharField(max_length=200, verbose_name='Seleção 3', default='Vencedor Jogo 59', blank=True, null=True)
    selecao4Semi = models.CharField(max_length=200, verbose_name='Seleção 4', default='Vencedor Jogo 60', blank=True, null=True)
    res25 = models.SmallIntegerField(blank=True, null=True)
    res26 = models.SmallIntegerField(blank=True, null=True)
    res27 = models.SmallIntegerField(blank=True, null=True)
    res28 = models.SmallIntegerField(blank=True, null=True)
    
    selecao1TerceiroLugar = models.CharField(max_length=200, verbose_name='Seleção 1', default='Perdedor Jogo 61', blank=True, null=True)
    selecao2TerceiroLugar = models.CharField(max_length=200, verbose_name='Seleção 2', default='Perdedor Jogo 62', blank=True, null=True)
    res29 = models.SmallIntegerField(blank=True, null=True)
    res30 = models.SmallIntegerField(blank=True, null=True)
    
    selecao1Final = models.CharField(max_length=200, verbose_name='Seleção 1', default='Vencedor Jogo 61', blank=True, null=True)
    selecao2Final = models.CharField(max_length=200, verbose_name='Seleção 2', default='Vencedor Jogo 62', blank=True, null=True)
    res31 = models.SmallIntegerField(blank=True, null=True)
    res32 = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Eliminatórias'
        verbose_name_plural = 'Eliminatórias'

    def __str__(self):
        return f'Eliminatórias'