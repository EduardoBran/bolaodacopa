from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from main.models import *

from .forms import RegistrationForm


def loginPage(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            'Você já se encontra logado.'
        )
        return redirect('main:pageindex')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"Bem vindo(a) {username}, você agora está logado e pode salvar seus palpites"
                    )
                    
                    if not GrupoA.objects.filter(usuario=request.user).exists():
                        GrupoA.objects.create(
                            usuario=user
                        )
                    if not GrupoB.objects.filter(usuario=request.user).exists():
                        GrupoB.objects.create(
                            usuario=user
                        )
                    if not GrupoC.objects.filter(usuario=request.user).exists():
                        GrupoC.objects.create(
                            usuario=user
                        )
                    if not GrupoD.objects.filter(usuario=request.user).exists():
                        GrupoD.objects.create(
                            usuario=user
                        )
                    if not GrupoE.objects.filter(usuario=request.user).exists():
                        GrupoE.objects.create(
                            usuario=user
                        )
                    if not GrupoF.objects.filter(usuario=request.user).exists():
                        GrupoF.objects.create(
                            usuario=user
                        )
                    if not GrupoG.objects.filter(usuario=request.user).exists():
                        GrupoG.objects.create(
                            usuario=user
                        )
                    if not GrupoH.objects.filter(usuario=request.user).exists():
                        GrupoH.objects.create(
                            usuario=user
                        )
                    if not Eliminatorias.objects.filter(usuario=request.user).exists():
                        Eliminatorias.objects.create(
                            usuario=user
                        )
                    if not PremioIndividual.objects.filter(usuario=request.user).exists():
                        PremioIndividual.objects.create(
                            usuario=user
                        )
                    if not PontuacaoUsuarios.objects.filter(usuario=request.user).exists():
                        PontuacaoUsuarios.objects.create(
                            usuario=user
                        )
                        
                    return redirect('main:pagemain')
                else:
                    return render(request, 'perfil/login.html', {"error": "Sua conta está desabilitada."})
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Usuário ou senha estão inválidos.'             
                )
                return render(request, 'perfil/login.html') 
        else:
            return render(request, 'perfil/login.html')


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(
            request,
            messages.WARNING,
            f'Usuário foi deslogado com sucesso.'
        )
        return redirect('main:pageindex')
    else:
        messages.add_message(
            request,
            messages.WARNING,
            f'Você já está deslogado.'
        )
        return redirect('main:pageindex')



def registerPage(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            f'Você já se encontra logado.'
        )
        return redirect('main:pageindex')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            form = RegistrationForm(request.POST or None)

            if form.is_valid():
                user = form.save()

                raw_password = form.cleaned_data.get('password1')

                user = authenticate(username=user.username, password=raw_password)

                if user is not None:
                    login(request, user)
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"Bem vindo(a) {username}, você está logado e pode salvar seus palpites."
                    )
                    if not GrupoA.objects.filter(usuario=request.user).exists():
                        GrupoA.objects.create(
                            usuario=user
                        )
                    if not GrupoB.objects.filter(usuario=request.user).exists():
                        GrupoB.objects.create(
                            usuario=user
                        )
                    if not GrupoC.objects.filter(usuario=request.user).exists():
                        GrupoC.objects.create(
                            usuario=user
                        )
                    if not GrupoD.objects.filter(usuario=request.user).exists():
                        GrupoD.objects.create(
                            usuario=user
                        )
                    if not GrupoE.objects.filter(usuario=request.user).exists():
                        GrupoE.objects.create(
                            usuario=user
                        )
                    if not GrupoF.objects.filter(usuario=request.user).exists():
                        GrupoF.objects.create(
                            usuario=user
                        )
                    if not GrupoG.objects.filter(usuario=request.user).exists():
                        GrupoG.objects.create(
                            usuario=user
                        )
                    if not GrupoH.objects.filter(usuario=request.user).exists():
                        GrupoH.objects.create(
                            usuario=user
                        )
                    if not Eliminatorias.objects.filter(usuario=request.user).exists():
                        Eliminatorias.objects.create(
                            usuario=user
                    )
                    if not PremioIndividual.objects.filter(usuario=request.user).exists():
                        PremioIndividual.objects.create(
                            usuario=user
                        )
                    if not PontuacaoUsuarios.objects.filter(usuario=request.user).exists():
                        PontuacaoUsuarios.objects.create(
                            usuario=user
                        )
                    return redirect('main:pagemain')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... você digitou algum campo inválido.'
                )
        else:
            form = RegistrationForm()

        context = {'form': form}
        return render(request, 'perfil/register.html', context)