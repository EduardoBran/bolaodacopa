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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
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
    
    primeiroColocado = models.CharField(max_length=200, verbose_name='Primeiro Lugar', default='', blank=True, null=True)
    segundoColocado = models.CharField(max_length=200, verbose_name='Segundo Lugar', default='', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Grupo H'
        verbose_name_plural = 'Grupo H'

    def __str__(self):
        return f'Grupo H'


class Eliminatorias(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    primeiroA = models.CharField(max_length=200, verbose_name='Primeiro A', default='Primeiro A', blank=True, null=True)
    segundoB = models.CharField(max_length=200, verbose_name='Segundo B', default='Segundo B', blank=True, null=True)
    primeiroC = models.CharField(max_length=200, verbose_name='Primeiro C', default='Primeiro C', blank=True, null=True)
    segundoD = models.CharField(max_length=200, verbose_name='Segundo D', default='Segundo D', blank=True, null=True)
    primeiroB = models.CharField(max_length=200, verbose_name='Primeiro B', default='Primeiro B', blank=True, null=True)
    segundoA = models.CharField(max_length=200, verbose_name='Segundo A', default='Segundo A', blank=True, null=True)
    primeiroD = models.CharField(max_length=200, verbose_name='Primeiro D', default='Primeiro D', blank=True, null=True)
    segundoC = models.CharField(max_length=200, verbose_name='Segundo C', default='Segundo C', blank=True, null=True)
    primeiroE = models.CharField(max_length=200, verbose_name='Primeiro E', default='Primeiro E', blank=True, null=True)
    segundoF = models.CharField(max_length=200, verbose_name='Segundo F', default='Segundo F', blank=True, null=True)
    primeiroG = models.CharField(max_length=200, verbose_name='Primeiro G', default='Primeiro G', blank=True, null=True)
    segundoH = models.CharField(max_length=200, verbose_name='Segundo H', default='Segundo H', blank=True, null=True)
    primeiroF = models.CharField(max_length=200, verbose_name='Primeiro F', default='Primeiro F', blank=True, null=True)
    segundoE = models.CharField(max_length=200, verbose_name='Segundo E', default='Segundo E', blank=True, null=True)
    primeiroH = models.CharField(max_length=200, verbose_name='Primeiro H', default='Primeiro H', blank=True, null=True)
    segundoG = models.CharField(max_length=200, verbose_name='Segundo G', default='Segundo G', blank=True, null=True)
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
    
    
class PremioIndividual(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    melhorJogador = models.CharField(max_length=50, verbose_name='Melhor Jogador', blank=True, null=True, default='')
    artilheiro = models.CharField(max_length=50, verbose_name='Melhor Jogador', blank=True, null=True, default='')
    artilheiroGols = models.SmallIntegerField(blank=True, null=True, verbose_name='Gols Artilheiro', default=0)
    melhorJogadorJovem = models.CharField(max_length=50, verbose_name='Melhor Jogador Jovem', blank=True, null=True, default='')
    
    class Meta:
        verbose_name = 'Premiação Individual'
        verbose_name_plural = 'Premiação Individual'

    def __str__(self):
        return f'Premiação Individual'


class PontuacaoUsuarios(Base):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    pontos = models.SmallIntegerField(verbose_name='Pontos', default=0)
    
    class Meta:
        verbose_name = 'Tabela Pts Usuários'
        verbose_name_plural = 'Tabela Pts Usuários'

    def __str__(self):
        return f'Tabela Pts Usuários'