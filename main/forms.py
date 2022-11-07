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