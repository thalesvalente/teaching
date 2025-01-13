

from django.contrib import admin
from django.urls import path, include
from app_farmacia import views  # import das funções presente na pasta views.py



urlpatterns = [
    path('admin/', admin.site.urls),    # path que redireciona para o adiministrador do Django
    path('', views.home,name='home'),   # path que redireciona para a tela inicial
    path('funcionarios/', views.funcionarios,name='funcionario'),  # path que redireciona para a area de funcionarios 
    path('estoque/', views.estoques,name='estoque'),    # path que redireciona para o estoque
    path('accounts/',include('django.contrib.auth.urls')),    # path que faz o login de usuarios
]
