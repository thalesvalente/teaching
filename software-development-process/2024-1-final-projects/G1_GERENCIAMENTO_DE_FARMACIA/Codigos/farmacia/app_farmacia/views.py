from django.shortcuts import render  # import da biblioteca para renderizar as paginas
from .models import Funcionario, Produto, Estoque   # importe do banco de dados
from django.contrib.auth.decorators import login_required   # import da tag de requisição de login

# tag para restringir o acesso somente a pessoas logadas ao sistema
@login_required  
def home(request):   #função para renderizar a pagina inicial
    return render(request,'app_farmacia/vendas.html')


#função para renderizar a area de funcionarios
@login_required
def funcionarios(request):      
    funcionarios = Funcionario.objects.all

    return render(request,'app_farmacia/ViewFuncionarios.html', {"funcionarios" : funcionarios})

#função para renderizar a area de estoque
@login_required
def estoques(request):      
    estoques = Estoque.objects.all
    return render(request,'app_farmacia/ViewEstoque.html', {"estoques" : estoques})




