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
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Qatar')
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Equador')
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Senegal')
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Holanda')
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
    selecao1 = models.CharField(max_length=200, verbose_name='Seleção 1', default='Qatar')
    selecao2 = models.CharField(max_length=200, verbose_name='Seleção 2', default='Equador')
    selecao3 = models.CharField(max_length=200, verbose_name='Seleção 3', default='Senegal')
    selecao4 = models.CharField(max_length=200, verbose_name='Seleção 4', default='Holanda')
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