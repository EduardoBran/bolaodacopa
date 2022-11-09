from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.PageIndex.as_view(), name='pageindex'),
    path('main/', views.PageMain.as_view(), name='pagemain'),
    path('main/grupoA/<int:pk>', views.PageGrupoA.as_view(), name='pagegrupoA'),
    path('main/grupoB/<int:pk>', views.PageGrupoB.as_view(), name='pagegrupoB'),
    path('main/grupoC/<int:pk>', views.PageGrupoC.as_view(), name='pagegrupoC'),
    path('main/grupoD/<int:pk>', views.PageGrupoD.as_view(), name='pagegrupoD'),
    path('main/grupoE/<int:pk>', views.PageGrupoE.as_view(), name='pagegrupoE'),
    path('main/grupoF/<int:pk>', views.PageGrupoF.as_view(), name='pagegrupoF'),
    path('main/grupoG/<int:pk>', views.PageGrupoG.as_view(), name='pagegrupoG'),
    path('main/grupoH/<int:pk>', views.PageGrupoH.as_view(), name='pagegrupoH'),
    path('main/eliminatoriasOitavas/<int:pk>', views.PageEliminatoriasOitavas.as_view(), name='eliminatoriasOitavas'),
    path('main/eliminatoriasQuartas/<int:pk>', views.PageEliminatoriasQuartas.as_view(), name='eliminatoriasQuartas'),
    path('salvartabelagrupoa/', views.SalvarTabelaGrupoA, name='salvartabelagrupoA'),
    path('salvartabelagrupob/', views.SalvarTabelaGrupoB, name='salvartabelagrupoB'),
    path('salvartabelagrupoc/', views.SalvarTabelaGrupoC, name='salvartabelagrupoC'),
    path('salvartabelagrupod/', views.SalvarTabelaGrupoD, name='salvartabelagrupoD'),
    path('salvartabelagrupoe/', views.SalvarTabelaGrupoE, name='salvartabelagrupoE'),
    path('salvartabelagrupof/', views.SalvarTabelaGrupoF, name='salvartabelagrupoF'),
    path('salvartabelagrupog/', views.SalvarTabelaGrupoG, name='salvartabelagrupoG'),
    path('salvartabelagrupoh/', views.SalvarTabelaGrupoH, name='salvartabelagrupoH'),
    path('salvareliminatoriasoitavas/', views.SalvarEliminatoriasOitavas, name='salvareliminatoriasoitavas'),
    path('salvareliminatoriasquartas/', views.SalvarEliminatoriasQuartas, name='salvareliminatoriasquartas'),
    
]
