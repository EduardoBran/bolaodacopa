from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .models import *


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
        context["bolaousergrupoB"] = GrupoA.objects.all().filter(
            usuario=self.request.user
        )
        return context
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(username=self.request.user)
        return qs

class PageIndex(TemplateView):
    template_name='main/index.html'

class PageMain(DispatchLoginRequiredMixin, TemplateView):
    template_name='main/main.html'