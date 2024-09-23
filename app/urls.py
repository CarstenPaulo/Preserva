from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('servicos', views.servicos, name='servicos'),
    path('contato', views.contato, name='contato'),
    
    #servicos
    path('aguas', views.aguas, name='aguas'),
    path('esgotos', views.esgotos, name='esgotos'),
    
    path('accesoria_ambiental', views.accesoria_ambiental, name='accesoria_ambiental'),
    path('residuos_solidos', views.residuos_solidos, name='residuos_solidos'),
    
    
    path('test', views.test, name='test'),
]
