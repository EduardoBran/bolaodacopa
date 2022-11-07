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
    

    

    

    

    
