from datetime import date, datetime, timedelta

from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from django.views import View
from django.views.generic import DetailView, TemplateView

from .forms import *
from .models import *


def CondicaoNomeSelecaoEliminatorias(selecao):
    if selecao == None or selecao == '':
        return False
    else:
        return True


class PageIndex(TemplateView):
    template_name='main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        dia_hoje = datetime.now()
        dia_hoje = dia_hoje.strftime('%d/%m/%Y %H:%M')
        dia_hoje = datetime.strptime(dia_hoje, '%d/%m/%Y %H:%M')
        
        dia_copa_do_mundo = '20/11/2022 13:00' 
        dia_copa_do_mundo = datetime.strptime(dia_copa_do_mundo, '%d/%m/%Y %H:%M')
        
        tempo_para_copa = dia_copa_do_mundo - dia_hoje
        tempo_para_copa = str(tempo_para_copa)
        tempo_para_copa = tempo_para_copa.replace(':', ' ')
        tempo_para_copa = tempo_para_copa.split()
        
        context['dia'] = tempo_para_copa[0]
        context['hora'] = tempo_para_copa[2]
        context['minuto'] = tempo_para_copa[3]
        
        return context


def sobreView(request):
    if str(request.method) == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            #chamando método de envio de email
            form.send_email()
            messages.success(request, 'Email enviado com sucesso.')
            form = ContatoForm()
        else:
            messages.error(request, 'Email NÃO FOI enviado com sucesso.')
    else:
        form = ContatoForm()

    context = {
        'form':form
    }
    return render(request, 'main/sobre.html', context)    

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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo A foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoA.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo A foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoA.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo A foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoA.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo B foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoB.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo B foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoB.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo B foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoB.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo C foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoC.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo C foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoC.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo C foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoC.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo D foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoD.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo D foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoD.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo D foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoD.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo E foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoE.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo E foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoE.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo E foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoE.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo F foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoF.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo F foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoF.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo F foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoF.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo G foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoG.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo G foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoG.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo G foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoG.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
    form = ResultadosGrupoHForm()
    
    if request.method == 'POST':
        form = ResultadosGrupoHForm(request.POST)
        
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
            
            primeiroColocado = form.cleaned_data['primeiroColocado']
            segundoColocado = form.cleaned_data['segundoColocado']
            
            if primeiroColocado == segundoColocado:
                if primeiroColocado == None and segundoColocado == None:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo H foi atualizada.'
                    )
                    return redirect('main:pagemain')
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Não pode escolher a mesma seleção para primeiro e segundo lugar respectivamente.'
                )
                return redirect('main:pagemain')
            
            else:
                if primeiroColocado == None:
                    GrupoH.objects.filter(usuario=request.user).update(
                        primeiroColocado='', segundoColocado=segundoColocado
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo H foi atualizada.'
                    )
                    return redirect('main:pagemain')
                if segundoColocado == None:
                    GrupoH.objects.filter(usuario=request.user).update(
                        primeiroColocado=primeiroColocado, segundoColocado=''
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Sua tabela do Grupo H foi atualizada.'
                    )
                    return redirect('main:pagemain')
            
            GrupoH.objects.filter(usuario=request.user).update(
                    primeiroColocado=primeiroColocado, segundoColocado=segundoColocado
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        primeiroColocadoA = list(GrupoA.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoA = primeiroColocadoA[0]['primeiroColocado']
        context['primeiroColocadoA'] = '1º Lugar Grupo A'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoA):
            context['primeiroColocadoA'] = primeiroColocadoA
        
        segundoColocadoA = list(GrupoA.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoA = segundoColocadoA[0]['segundoColocado']
        context['segundoColocadoA'] = '2º Lugar Grupo A'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoA):
            context['segundoColocadoA'] = segundoColocadoA
        
        primeiroColocadoB = list(GrupoB.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoB = primeiroColocadoB[0]['primeiroColocado']
        context['primeiroColocadoB'] = '1º Lugar Grupo B'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoB):
            context['primeiroColocadoB'] = primeiroColocadoB
        
        segundoColocadoB = list(GrupoB.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoB = segundoColocadoB[0]['segundoColocado']
        context['segundoColocadoB'] = '2º Lugar Grupo B'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoB):
            context['segundoColocadoB'] = segundoColocadoB
        
        primeiroColocadoC = list(GrupoC.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoC = primeiroColocadoC[0]['primeiroColocado']
        context['primeiroColocadoC'] = '1º Lugar Grupo C'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoC):
            context['primeiroColocadoC'] = primeiroColocadoC
        
        segundoColocadoC = list(GrupoC.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoC = segundoColocadoC[0]['segundoColocado']
        context['segundoColocadoC'] = '2º Lugar Grupo C'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoC):
            context['segundoColocadoC'] = segundoColocadoC
        
        primeiroColocadoD = list(GrupoD.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoD = primeiroColocadoD[0]['primeiroColocado']
        context['primeiroColocadoD'] = '1º Lugar Grupo D'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoD):
            context['primeiroColocadoD'] = primeiroColocadoD
        
        segundoColocadoD = list(GrupoD.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoD = segundoColocadoD[0]['segundoColocado']
        context['segundoColocadoD'] = '2º Lugar Grupo D'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoD):
            context['segundoColocadoD'] = segundoColocadoD
        
        primeiroColocadoE = list(GrupoE.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoE = primeiroColocadoE[0]['primeiroColocado']
        context['primeiroColocadoE'] = '1º Lugar Grupo E'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoE):
            context['primeiroColocadoE'] = primeiroColocadoE
        
        segundoColocadoE = list(GrupoE.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoE = segundoColocadoE[0]['segundoColocado']
        context['segundoColocadoE'] = '2º Lugar Grupo E'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoE):
            context['segundoColocadoE'] = segundoColocadoE
        
        primeiroColocadoF = list(GrupoF.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoF = primeiroColocadoF[0]['primeiroColocado']
        context['primeiroColocadoF'] = '1º Lugar Grupo F'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoF):
            context['primeiroColocadoF'] = primeiroColocadoF
        
        segundoColocadoF = list(GrupoF.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoF = segundoColocadoF[0]['segundoColocado']
        context['segundoColocadoF'] = '2º Lugar Grupo F'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoF):
            context['segundoColocadoF'] = segundoColocadoF
        
        primeiroColocadoG = list(GrupoG.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoG = primeiroColocadoG[0]['primeiroColocado']
        context['primeiroColocadoG'] = '1º Lugar Grupo G'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoG):
            context['primeiroColocadoG'] = primeiroColocadoG
        
        segundoColocadoG = list(GrupoG.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoG = segundoColocadoG[0]['segundoColocado']
        context['segundoColocadoG'] = '2º Lugar Grupo G'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoG):
            context['segundoColocadoG'] = segundoColocadoG
        
        primeiroColocadoH = list(GrupoH.objects.filter(usuario=self.request.user).values('primeiroColocado'))
        primeiroColocadoH = primeiroColocadoH[0]['primeiroColocado']
        context['primeiroColocadoH'] = '1º Lugar Grupo H'
        if CondicaoNomeSelecaoEliminatorias(primeiroColocadoH):
            context['primeiroColocadoH'] = primeiroColocadoH
        
        segundoColocadoH = list(GrupoH.objects.filter(usuario=self.request.user).values('segundoColocado'))
        segundoColocadoH = segundoColocadoH[0]['segundoColocado']
        context['segundoColocadoH'] = '2º Lugar Grupo H'
        if CondicaoNomeSelecaoEliminatorias(segundoColocadoH):
            context['segundoColocadoH'] = segundoColocadoH
        
        Eliminatorias.objects.filter(usuario=self.request.user).update(
                    primeiroA=primeiroColocadoA, segundoB=segundoColocadoB, primeiroC=primeiroColocadoC, segundoD=segundoColocadoD,
                    primeiroB=primeiroColocadoB, segundoA=segundoColocadoA, primeiroD=primeiroColocadoD, segundoC=segundoColocadoC,
                    primeiroE=primeiroColocadoE, segundoF=segundoColocadoF, primeiroG=primeiroColocadoG, segundoH=segundoColocadoH,
                    primeiroF=primeiroColocadoF, segundoE=segundoColocadoE, primeiroH=primeiroColocadoH, segundoG=segundoColocadoG,
                )
        
        return context


def SalvarEliminatoriasOitavas(request):
    form = ResultadosEliminatoriasOitavasForm()
    
    if request.method == 'POST':
        form = ResultadosEliminatoriasOitavasForm(request.POST)
        
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
            res13 = form.cleaned_data['res13']
            res14 = form.cleaned_data['res14']
            res15 = form.cleaned_data['res15']
            res16 = form.cleaned_data['res16']
            
            if not res1 == None or not res2 == None:
                if res1 == res2:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2
                )
            
            if not res3 == None or not res4 == None: 
                if res3 == res4:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res3=res3, res4=res4
                )
            
            if not res5 == None or not res6 == None: 
                if res5 == res6:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res5=res5, res6=res6
                )
            
            if not res7 == None or not res8 == None: 
                if res7 == res8:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res7=res7, res8=res8
                )
            
            if not res9 == None or not res10 == None: 
                if res9 == res10:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res9=res9, res10=res10
                )
            
            if not res11 == None or not res12 == None: 
                if res11 == res12:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res11=res11, res12=res12
                )
            
            if not res13 == None or not res14 == None: 
                if res13 == res14:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res13=res13, res14=res14
                )
            
            if not res15 == None or not res16 == None: 
                if res15 == res16:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res15=res15, res16=res16
                )
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res1=res1, res2=res2, res3=res3, res4=res4,
                    res5=res5, res6=res6, res7=res7, res8=res8, 
                    res9=res9, res10=res10, res11=res11, res12=res12,
                    res13=res13, res14=res14, res15=res15, res16=res16
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela das oitavas de final foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/eliminatoriasOitavas.html', {'form': form})
    
        
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
        
        if res1 == None or res2 == None:
            context['selecao1quartas'] = 'Vencedor Jogo 49' 
        
        elif res1 > res2:    
            primeiroA = Eliminatorias.objects.filter(usuario=self.request.user).values('primeiroA')
            primeiroA = list(primeiroA)
            primeiroA = primeiroA[0]['primeiroA']
            
            if primeiroA == None:
                primeiroA = 'Vencedor Jogo 49'
            
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
        
        if res3 == None or res4 == None:
            context['selecao2quartas'] = 'Vencedor Jogo 50' 
            
        elif res3 > res4:    
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
        
        if res5 == None or res6 == None:
            context['selecao3quartas'] = 'Vencedor Jogo 51'
        
        elif res5 > res6:    
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
            
        if res7 == None or res8 == None:
            context['selecao4quartas'] = 'Vencedor Jogo 52'
            
        elif res7 > res8:    
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
        
        if res9 == None or res10 == None:
            context['selecao5quartas'] = 'Vencedor Jogo 53'
        
        elif res9 > res10:    
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
        
        if res11 == None or res12 == None:
            context['selecao6quartas'] = 'Vencedor Jogo 54'
        
        elif res11 > res12:    
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
        
        if res13 == None or res14 == None:
            context['selecao7quartas'] = 'Vencedor Jogo 55'
        
        elif res13 > res14:    
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
        
        if res15 == None or res16 == None:
            context['selecao8quartas'] = 'Vencedor Jogo 56'
        
        elif res15 > res16:    
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


def SalvarEliminatoriasQuartas(request):
    form = ResultadosEliminatoriasQuartasForm()
    
    if request.method == 'POST':
        form = ResultadosEliminatoriasQuartasForm(request.POST)
        
        if form.is_valid():
            res17 = form.cleaned_data['res17']
            res18 = form.cleaned_data['res18']
            res19 = form.cleaned_data['res19']
            res20 = form.cleaned_data['res20']
            res21 = form.cleaned_data['res21']
            res22 = form.cleaned_data['res22']
            res23 = form.cleaned_data['res23']
            res24 = form.cleaned_data['res24']
            
            if not res17 == None or not res18 == None:
                if res17 == res18:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res17=res17, res18=res18
                )
            
            if not res19 == None or not res20 == None:
                if res19 == res20:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res19=res19, res20=res20
                )
            
            if not res21 == None or not res22 == None:
                if res21 == res22:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res21=res21, res22=res22
                )
            
            if not res23 == None or not res24 == None:
                if res23 == res24:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res23=res23, res24=res24
                )
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res17=res17, res18=res18, res19=res19, res20=res20,
                    res21=res21, res22=res22, res23=res23, res24=res24
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela das quartas de final foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/eliminatoriasQuartas.html', {'form': form})
    

class PageEliminatoriasSemi(DispatchLoginRequiredMixin, DetailView):
    model = Eliminatorias
    template_name = 'main/eliminatoriasSemi.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        res17 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res17'))
        res17 = res17[0]['res17']
        res18 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res18'))
        res18 = res18[0]['res18']
        res19 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res19'))
        res19 = res19[0]['res19']
        res20 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res20'))
        res20 = res20[0]['res20']
        res21 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res21'))
        res21 = res21[0]['res21']
        res22 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res22'))
        res22 = res22[0]['res22']
        res23 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res23'))
        res23 = res23[0]['res23']
        res24 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res24'))
        res24 = res24[0]['res24']
        
        if res17 == None or res18 == None:
            context['selecao1Semi'] = 'Vencedor Jogo 57' 
        
        elif res17 > res18:
            selecao1Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao1Quartas'))
            selecao1Quartas = selecao1Quartas[0]['selecao1Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao1Semi=selecao1Quartas
            )
            context['selecao1Semi'] = selecao1Quartas
        elif res18 > res17:
            selecao2Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao2Quartas'))
            selecao2Quartas = selecao2Quartas[0]['selecao2Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao1Semi=selecao2Quartas
            )
            context['selecao1Semi'] = selecao2Quartas
        
        if res19 == None or res20 == None:
            context['selecao2Semi'] = 'Vencedor Jogo 58'
        
        elif res19 > res20:
            selecao3Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao3Quartas'))
            selecao3Quartas = selecao3Quartas[0]['selecao3Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao2Semi=selecao3Quartas
            )
            context['selecao2Semi'] = selecao3Quartas
        elif res20 > res19:
            selecao4Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao4Quartas'))
            selecao4Quartas = selecao4Quartas[0]['selecao4Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao2Semi=selecao4Quartas
            )
            context['selecao2Semi'] = selecao4Quartas
        
        if res21 == None or res22 == None:
            context['selecao3Semi'] = 'Vencedor Jogo 59'
        
        elif res21 > res22:
            selecao5Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao5Quartas'))
            selecao5Quartas = selecao5Quartas[0]['selecao5Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao3Semi=selecao5Quartas
            )
            context['selecao3Semi'] = selecao5Quartas
        elif res22 > res21:
            selecao6Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao6Quartas'))
            selecao6Quartas = selecao6Quartas[0]['selecao6Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao3Semi=selecao6Quartas
            )
            context['selecao3Semi'] = selecao6Quartas
        
        if res23 == None or res24 == None:
            context['selecao4Semi'] = 'Vencedor Jogo 60'
        
        elif res23 > res24:
            selecao7Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao7Quartas'))
            selecao7Quartas = selecao7Quartas[0]['selecao7Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao4Semi=selecao7Quartas
            )
            context['selecao4Semi'] = selecao7Quartas
        elif res24 > res23:
            selecao8Quartas = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao8Quartas'))
            selecao8Quartas = selecao8Quartas[0]['selecao8Quartas']
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao4Semi=selecao8Quartas
            )
            context['selecao4Semi'] = selecao8Quartas
        
        return context
    
def SalvarEliminatoriasSemi(request):
    form = ResultadosEliminatoriasSemiForm()
    
    if request.method == 'POST':
        form = ResultadosEliminatoriasSemiForm(request.POST)
        
        if form.is_valid():
            res25 = form.cleaned_data['res25']
            res26 = form.cleaned_data['res26']
            res27 = form.cleaned_data['res27']
            res28 = form.cleaned_data['res28']
            
            if not res25 == None or not res26 == None:
                if res25 == res26:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res25=res25, res26=res26
                )
            
            if not res27 == None or not res28 == None:
                if res27 == res28:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res27=res27, res28=res28
                )
            
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res25=res25, res26=res26, res27=res27, res28=res28
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela da semi final foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/eliminatoriasSemi.html', {'form': form})


class PageEliminatoriasFinal(DispatchLoginRequiredMixin, DetailView):
    model = Eliminatorias
    template_name = 'main/eliminatoriasFinal.html'
    context_object_name = 'info'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        res25 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res25'))
        res25 = res25[0]['res25']
        res26 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res26'))
        res26 = res26[0]['res26']
        res27 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res27'))
        res27 = res27[0]['res27']
        res28 = list(Eliminatorias.objects.filter(usuario=self.request.user).values('res28'))
        res28 = res28[0]['res28']
        
        selecao1Semi = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao1Semi'))
        selecao1Semi = selecao1Semi[0]['selecao1Semi']
        selecao2Semi = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao2Semi'))
        selecao2Semi = selecao2Semi[0]['selecao2Semi']
        selecao3Semi = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao3Semi'))
        selecao3Semi = selecao3Semi[0]['selecao3Semi']
        selecao4Semi = list(Eliminatorias.objects.filter(usuario=self.request.user).values('selecao4Semi'))
        selecao4Semi = selecao4Semi[0]['selecao4Semi']
        
        if res25 == None or res26 == None:
            context['selecao1Final'] = 'Vencedor Jogo 61'
            context['selecao1TerceiroLugar'] = 'Perdedor Jogo 61'
            
        elif res25 > res26:
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao1Final=selecao1Semi, selecao1TerceiroLugar=selecao2Semi
            )
            context['selecao1Final'] = selecao1Semi
            context['selecao1TerceiroLugar'] = selecao2Semi
        elif res26 > res25:
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao1Final=selecao2Semi, selecao1TerceiroLugar=selecao1Semi
            )
            context['selecao1Final'] = selecao2Semi
            context['selecao1TerceiroLugar'] = selecao1Semi
        
        if res27 == None or res28 == None:
            context['selecao2Final'] = 'Vencedor Jogo 62'
            context['selecao2TerceiroLugar'] = 'Perdedor Jogo 62'
            
        elif res27 > res28:
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao2Final=selecao3Semi, selecao2TerceiroLugar=selecao4Semi
            )
            context['selecao2Final'] = selecao3Semi
            context['selecao2TerceiroLugar'] = selecao4Semi
        elif res28 > res27:
            Eliminatorias.objects.filter(usuario=self.request.user).update(
                selecao1Final=selecao4Semi, selecao1TerceiroLugar=selecao3Semi
            )
            context['selecao2Final'] = selecao4Semi
            context['selecao2TerceiroLugar'] = selecao3Semi
            
        return context


def SalvarEliminatoriasFinal(request):
    form = ResultadosEliminatoriasFinaisForm()
    
    if request.method == 'POST':
        form = ResultadosEliminatoriasFinaisForm(request.POST)
        
        if form.is_valid():
            res29 = form.cleaned_data['res29']
            res30 = form.cleaned_data['res30']
            res31 = form.cleaned_data['res31']
            res32 = form.cleaned_data['res32']
            
            if not res29 == None or not res30 == None:
                if res29 == res30:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res29=res29, res30=res30
                )
            
            if not res31 == None or not res32 == None:
                if res31 == res32:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'Este jogo precisa ter um ganhador.'
                    )
                    return redirect('main:pagemain')
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res31=res31, res32=res32
                )
            
            Eliminatorias.objects.filter(usuario=request.user).update(
                    res29=res29, res30=res30, res31=res31, res32=res32
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Sua tabela das finais foi atualizada.'
            )
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/eliminatoriasFinal.html', {'form': form})