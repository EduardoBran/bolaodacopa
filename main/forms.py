from django import forms

from .models import *


class ResultadosGrupoAForm(forms.ModelForm):
    class Meta:
        model = GrupoA
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosGrupoBForm(forms.ModelForm):
    class Meta:
        model = GrupoB
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosGrupoCForm(forms.ModelForm):
    class Meta:
        model = GrupoC
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosGrupoDForm(forms.ModelForm):
    class Meta:
        model = GrupoD
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )
        
class ResultadosGrupoEForm(forms.ModelForm):
    class Meta:
        model = GrupoE
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosGrupoFForm(forms.ModelForm):
    class Meta:
        model = GrupoF
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosGrupoGForm(forms.ModelForm):
    class Meta:
        model = GrupoG
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosGrupoHForm(forms.ModelForm):
    class Meta:
        model = GrupoH
        fields = ('res1', 'res2', 'res3',
                  'res4', 'res5', 'res6',
                  'res7', 'res8', 'res9',
                  'res10', 'res11', 'res12',
                  'primeiroColocado', 'segundoColocado'
                  )

class ResultadosEliminatoriasOitavasForm(forms.ModelForm):
    class Meta:
        model = Eliminatorias
        fields = ('res1', 'res2', 'res3', 'res4',
                  'res5', 'res6', 'res7', 'res8',
                  'res9', 'res10', 'res11', 'res12',
                  'res13', 'res14', 'res15', 'res16'
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