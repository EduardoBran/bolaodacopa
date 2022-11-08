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
