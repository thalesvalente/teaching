from django.db import models

# Criação do banco de dados

# criação da classe funcionario 
class Funcionario(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(verbose_name= 'Nome', max_length=250)
    cpf=models.CharField(verbose_name= 'CPF', max_length=250)
    telefone=models.CharField(verbose_name= 'Telefone', max_length=250)
    endereco=models.CharField(verbose_name= 'Endereço', max_length=250)
    dataNasc=models.DateField(verbose_name= 'Data de Nascimento', )
    email=models.CharField(verbose_name= 'E-mail', max_length=250)
    cargo=models.CharField(verbose_name= 'Cargo', max_length=250)
    dataAdmissao=models.DateField(verbose_name= 'Data de Admissão', )
    salario=models.FloatField(verbose_name= 'Salário', )
    

# criação da classe produto 
class Produto(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(verbose_name= 'Nome', max_length=250)
    descricao=models.CharField(verbose_name= 'Descrição', max_length=500)
    preco=models.FloatField(verbose_name= 'Preço',)
    categoria=models.CharField(verbose_name= 'Categoria', max_length=250)
    dataValidade=models.DateField(verbose_name= 'Data de Validade', )
    nomeForncedor=models.CharField(verbose_name= 'Nome do Fornecedor', max_length=250, null=True)
    emailFornecedor=models.CharField(verbose_name= 'E-mail do Fornecedor', max_length=250, null=True)
    prescricao=models.BooleanField(verbose_name= 'Prescrição',null=True )
    

# criação da classe estoque 
class Estoque(models.Model):
    id=models.AutoField(primary_key=True)
    idProduto=models.ForeignKey(Produto,on_delete=models.CASCADE, verbose_name= 'Código do Produto', )
    quantidade=models.IntegerField(verbose_name= 'Quantidade', )
    qtdMinima=models.IntegerField(verbose_name= 'Quantidade Mínima', null=True)


# criação da classe cliente 
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(verbose_name= 'Nome', max_length=250)
    cpf=models.CharField(verbose_name= 'CPF', max_length=250)
    telefone=models.CharField(verbose_name= 'Telefone', max_length=250)


# criação da classe vendas 
class Venda(models.Model):
    id=models.AutoField(primary_key=True)
    idFuncionario=models.ForeignKey(Funcionario,on_delete=models.CASCADE, verbose_name= 'Código do Funcionário', )
    nomeCliente=models.CharField(verbose_name= 'Nome do Cliente', max_length=250)
    itens=models.CharField(verbose_name= 'Itens da Venda', max_length=1000)
    total=models.FloatField()
    metodoPagamento=models.CharField(max_length=250)
