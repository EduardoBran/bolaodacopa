from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, TemplateView

from .forms import *
from .models import *


class PageIndex(TemplateView):
    template_name='main/index.html'
    

class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(
                self.request,
                'Necessário efetuar o login para salvar/editar o seu bolão.'
            )
            return redirect('perfil:login')
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bolaousergrupoA"] = GrupoA.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoB"] = GrupoB.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoC"] = GrupoC.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoD"] = GrupoD.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoE"] = GrupoE.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoF"] = GrupoF.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoG"] = GrupoG.objects.all().filter(
            usuario=self.request.user
        )
        context["bolaousergrupoH"] = GrupoH.objects.all().filter(
            usuario=self.request.user
        )
        context["eliminatorias"] = Eliminatorias.objects.all().filter(
            usuario=self.request.user
        )
        return context
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs
    

class PageMain(DispatchLoginRequiredMixin, TemplateView):
    template_name='main/main.html'
    
    
class PageGrupoA(DispatchLoginRequiredMixin, DetailView):
    model = GrupoA
    template_name = 'main/grupoA.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'


def SalvarTabelaGrupoA(request):
    form = ResultadosGrupoAForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoAForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoA.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo A foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoA.html', {'form': form})    
            

class PageGrupoB(DispatchLoginRequiredMixin, DetailView):
    model = GrupoB
    template_name = 'main/grupoB.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoB(request):
    form = ResultadosGrupoBForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoBForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoB.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo B foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoB.html', {'form': form})    


class PageGrupoC(DispatchLoginRequiredMixin, DetailView):
    model = GrupoC
    template_name = 'main/grupoC.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoC(request):
    form = ResultadosGrupoCForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoCForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoC.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo C foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoC.html', {'form': form})    


class PageGrupoD(DispatchLoginRequiredMixin, DetailView):
    model = GrupoD
    template_name = 'main/grupoD.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoD(request):
    form = ResultadosGrupoDForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoDForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoD.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo D foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoD.html', {'form': form})    


class PageGrupoE(DispatchLoginRequiredMixin, DetailView):
    model = GrupoE
    template_name = 'main/grupoE.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoE(request):
    form = ResultadosGrupoEForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoEForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoE.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo E foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoE.html', {'form': form})    


class PageGrupoF(DispatchLoginRequiredMixin, DetailView):
    model = GrupoF
    template_name = 'main/grupoF.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoF(request):
    form = ResultadosGrupoFForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoFForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoF.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo F foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoF.html', {'form': form})    


class PageGrupoG(DispatchLoginRequiredMixin, DetailView):
    model = GrupoG
    template_name = 'main/grupoG.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoG(request):
    form = ResultadosGrupoGForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoGForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoG.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo G foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoG.html', {'form': form})    


class PageGrupoH(DispatchLoginRequiredMixin, DetailView):
    model = GrupoH
    template_name = 'main/grupoH.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    

def SalvarTabelaGrupoH(request):
    form = ResultadosGrupoCForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoCForm(request.POST)
        
        if form.is_valid():
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            
            GrupoH.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
                    res6=res6, res7=res7, res8=res8, res9=res9,
                    res10=res10, res11=res11, res12=res12
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo H foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoH.html', {'form': form})    



class PageEliminatoriasOitavas(DispatchLoginRequiredMixin, DetailView):
    model = Eliminatorias
    template_name = 'main/eliminatoriasOitavas.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'

def SalvarEliminatoriasOitavas(request):
    form = ResultadosEliminatoriasOitavas()
    
    if request.method == 'POST':
        form = ResultadosEliminatoriasOitavas(request.POST)
        
        if form.is_valid():
            primeiroA = form.cleaned_data['primeiroA']
            res1 = form.cleaned_data['res1']
            res2 = form.cleaned_data['res2']
            segundoB = form.cleaned_data['segundoB']
            primeiroC = form.cleaned_data['primeiroC']
            res3 = form.cleaned_data['res3']
            res4 = form.cleaned_data['res4']
            segundoD = form.cleaned_data['segundoD']
            primeiroB = form.cleaned_data['primeiroB']
            res5 = form.cleaned_data['res5']
            res6 = form.cleaned_data['res6']
            segundoA = form.cleaned_data['segundoA']
            primeiroD = form.cleaned_data['primeiroD']
            res7 = form.cleaned_data['res7']
            res8 = form.cleaned_data['res8']
            segundoC = form.cleaned_data['segundoC']
            primeiroE = form.cleaned_data['primeiroE']
            res9 = form.cleaned_data['res9']
            res10 = form.cleaned_data['res10']
            segundoF = form.cleaned_data['segundoF']
            primeiroG = form.cleaned_data['primeiroG']
            res11 = form.cleaned_data['res11']
            res12 = form.cleaned_data['res12']
            segundoH = form.cleaned_data['segundoH']
            primeiroF = form.cleaned_data['primeiroF']
            res13 = form.cleaned_data['res13']
            res14 = form.cleaned_data['res14']
            segundoE = form.cleaned_data['segundoE']
            primeiroH = form.cleaned_data['primeiroH']
            res15 = form.cleaned_data['res15']
            res16 = form.cleaned_data['res16']
            segundoG = form.cleaned_data['segundoG']
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    primeiroA=primeiroA, res1=res1, res2=res2, segundoB=segundoB,
                    primeiroC=primeiroC, res3=res3, res4=res4, segundoD=segundoD,
                    primeiroB=primeiroB, res5=res5, res6=res6, segundoA=segundoA,
                    primeiroD=primeiroD, res7=res7, res8=res8, segundoC=segundoC,
                    primeiroE=primeiroE, res9=res9, res10=res10, segundoF=segundoF,
                    primeiroG=primeiroG, res11=res11, res12=res12, segundoH=segundoH,
                    primeiroF=primeiroF, res13=res13, res14=res14, segundoE=segundoE,
                    primeiroH=primeiroH, res15=res15, res16=res16, segundoG=segundoG,
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela do Grupo H foi atualizada.'
            )
            return redirect('main:pagemain')
        
class PageEliminatoriasQuartas(DispatchLoginRequiredMixin, DetailView):
    model = Eliminatorias
    template_name = 'main/eliminatoriasQuartas.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        res1 = Eliminatorias.objects.filter(usuario=self.request.user).values('res1')
        res1 = list(res1)
        res1 = res1[0]['res1']
        res2 = Eliminatorias.objects.filter(usuario=self.request.user).values('res2')
        res2 = list(res2)
        res2 = res2[0]['res2']
        res3 = Eliminatorias.objects.filter(usuario=self.request.user).values('res3')
        res3 = list(res3)
        res3 = res3[0]['res3']
        res4 = Eliminatorias.objects.filter(usuario=self.request.user).values('res4')
        res4 = list(res4)
        res4 = res4[0]['res4']
        res5 = Eliminatorias.objects.filter(usuario=self.request.user).values('res5')
        res5 = list(res5)
        res5 = res5[0]['res5']
        res6 = Eliminatorias.objects.filter(usuario=self.request.user).values('res6')
        res6 = list(res6)
        res6 = res6[0]['res6']
        res7 = Eliminatorias.objects.filter(usuario=self.request.user).values('res7')
        res7 = list(res7)
        res7 = res7[0]['res7']
        res8 = Eliminatorias.objects.filter(usuario=self.request.user).values('res8')
        res8 = list(res8)
        res8 = res8[0]['res8']
        res9 = Eliminatorias.objects.filter(usuario=self.request.user).values('res9')
        res9 = list(res9)
        res9 = res9[0]['res9']
        res10 = Eliminatorias.objects.filter(usuario=self.request.user).values('res10')
        res10 = list(res10)
        res10 = res10[0]['res10']
        res11 = Eliminatorias.objects.filter(usuario=self.request.user).values('res11')
        res11 = list(res11)
        res11 = res11[0]['res11']
        res12 = Eliminatorias.objects.filter(usuario=self.request.user).values('res12')
        res12 = list(res12)
        res12 = res12[0]['res12']
        res13 = Eliminatorias.objects.filter(usuario=self.request.user).values('res13')
        res13 = list(res13)
        res13 = res13[0]['res13']
        res14 = Eliminatorias.objects.filter(usuario=self.request.user).values('res14')
        res14 = list(res14)
        res14 = res14[0]['res14']
        res15 = Eliminatorias.objects.filter(usuario=self.request.user).values('res15')
        res15 = list(res15)
        res15 = res15[0]['res15']
        res16 = Eliminatorias.objects.filter(usuario=self.request.user).values('res16')
        res16 = list(res16)
        res16 = res16[0]['res16']
        
        if res1 > res2:    
            primeiroA = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroA')
            primeiroA = list(primeiroA)
            primeiroA = primeiroA[0]['primeiroA']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao1Quartas=primeiroA
                )
            context['selecao1quartas'] = primeiroA 
        elif res2 > res1:
            segundoB = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoB')
            segundoB = list(segundoB)
            segundoB = segundoB[0]['segundoB']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao1Quartas=segundoB
                )
            context['selecao1quartas'] = segundoB
            
        if res3 > res4:    
            primeiroC = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroC')
            primeiroC = list(primeiroC)
            primeiroC = primeiroC[0]['primeiroC']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao2Quartas=primeiroC
                )
            context['selecao2quartas'] = primeiroC     
        elif res4 > res3:
            segundoD = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoD')
            segundoD = list(segundoD)
            segundoD = segundoD[0]['segundoD']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao2Quartas=segundoD
                )
            context['selecao2quartas'] = segundoD
        
        if res5 > res6:    
            primeiroB = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroB')
            primeiroB = list(primeiroB)
            primeiroB = primeiroB[0]['primeiroB']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao3Quartas=primeiroB
                )
            context['selecao3quartas'] = primeiroB     
        elif res6 > res5:
            segundoA = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoA')
            segundoA = list(segundoA)
            segundoA = segundoA[0]['segundoA']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao3Quartas=segundoA
                )
            context['selecao3quartas'] = segundoA
        
        if res7 > res8:    
            primeiroD = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroD')
            primeiroD = list(primeiroD)
            primeiroD = primeiroD[0]['primeiroD']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao4Quartas=primeiroD
                )
            context['selecao4quartas'] = primeiroD     
        elif res8 > res7:
            segundoC = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoC')
            segundoC = list(segundoC)
            segundoC = segundoC[0]['segundoC']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao4Quartas=segundoC
                )
            context['selecao4quartas'] = segundoC
        
        if res9 > res10:    
            primeiroE = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroE')
            primeiroE = list(primeiroE)
            primeiroE = primeiroE[0]['primeiroE']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao5Quartas=primeiroE
                )
            context['selecao5quartas'] = primeiroE     
        elif res10 > res9:
            segundoF = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoF')
            segundoF = list(segundoF)
            segundoF = segundoF[0]['segundoF']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao5Quartas=segundoF
                )
            context['selecao5quartas'] = segundoF
        
        if res11 > res12:    
            primeiroG = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroG')
            primeiroG = list(primeiroG)
            primeiroG = primeiroG[0]['primeiroG']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao6Quartas=primeiroG
                )
            context['selecao6quartas'] = primeiroG     
        elif res12 > res11:
            segundoH = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoH')
            segundoH = list(segundoH)
            segundoH = segundoH[0]['segundoH']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao6Quartas=segundoH
                )
            context['selecao6quartas'] = segundoH
        
        if res13 > res14:    
            primeiroF = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroF')
            primeiroF = list(primeiroF)
            primeiroF = primeiroF[0]['primeiroF']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao7Quartas=primeiroF
                )
            context['selecao7quartas'] = primeiroF     
        elif res14 > res13:
            segundoE = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoE')
            segundoE = list(segundoE)
            segundoE = segundoE[0]['segundoE']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao7Quartas=segundoE
                )
            context['selecao7quartas'] = segundoE
        
        if res15 > res16:    
            primeiroH = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroH')
            primeiroH = list(primeiroH)
            primeiroH = primeiroH[0]['primeiroH']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao8Quartas=primeiroH
                )
            context['selecao8quartas'] = primeiroH     
        elif res16 > res15:
            segundoG = Eliminatorias.objects.filter(usuario=self.request.user).values('segundoG')
            segundoG = list(segundoG)
            segundoG = segundoG[0]['segundoG']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                    selecao8Quartas=segundoG
                )
            context['selecao8quartas'] = segundoG
        
        return context