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