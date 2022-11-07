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
            return redirect('main:pagemain')
        
    elif request.method == 'GET':
        return render(request, 'main/grupoB.html', {'form': form})    
