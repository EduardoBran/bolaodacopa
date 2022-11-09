from django import forms

from .models import *


class ResultadosGrupoAForm(forms.ModelForm):
    class Meta:
        model = GrupoA
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosGrupoBForm(forms.ModelForm):
    class Meta:
        model = GrupoB
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosGrupoCForm(forms.ModelForm):
    class Meta:
        model = GrupoC
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosGrupoDForm(forms.ModelForm):
    class Meta:
        model = GrupoD
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )
        
class ResultadosGrupoEForm(forms.ModelForm):
    class Meta:
        model = GrupoE
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosGrupoFForm(forms.ModelForm):
    class Meta:
        model = GrupoF
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosGrupoGForm(forms.ModelForm):
    class Meta:
        model = GrupoG
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosGrupoHForm(forms.ModelForm):
    class Meta:
        model = GrupoH
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12'
                  )

class ResultadosEliminatoriasOitavasForm(forms.ModelForm):
    class Meta:
        model = Eliminatorias
        fields = ('primeiroA', 'res1', 'res2', 'segundoB',
                  'primeiroC', 'res3', 'res4', 'segundoD',
                  'primeiroB', 'res5', 'res6', 'segundoA',
                  'primeiroD', 'res7', 'res8', 'segundoC',
                  'primeiroE', 'res9', 'res10', 'segundoF',
                  'primeiroG', 'res11', 'res12', 'segundoH',
                  'primeiroF', 'res13', 'res14', 'segundoE',
                  'primeiroH', 'res15', 'res16', 'segundoG',
                  )

class ResultadosEliminatoriasQuartasForm(forms.ModelForm):
    class Meta:
        model = Eliminatorias
        fields = ('res17', 'res18', 'res19', 'res20',
                  'res21', 'res22', 'res23', 'res24',
                  )

class ResultadosEliminatoriasSemiForm(forms.ModelForm):
    class Meta:
        model = Eliminatorias
        fields = ('res25', 'res26', 'res27', 'res28')
        
class ResultadosEliminatoriasFinaisForm(forms.ModelForm):
    class Meta:
        model = Eliminatorias
        fields = ('res29', 'res30', 'res31', 'res32')