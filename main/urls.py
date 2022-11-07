from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.PageIndex.as_view(), name='pageindex'),
    path('main/', views.PageMain.as_view(), name='pagemain'),
    path('main/grupoA/<int:pk>', views.PageGrupoA.as_view(), name='pagegrupoA'),
    path('main/grupoB/<int:pk>', views.PageGrupoB.as_view(), name='pagegrupoB'),
]
