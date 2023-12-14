<?php

namespace App\Http\Controllers;

use App\Models\Cliente;
use App\Models\Funcionario;
use Illuminate\Http\Request;
use App\Models\Locacao;
use App\Models\Veiculo;

class LocacaoController extends Controller
{
    // Método para exibir a view de consulta de locações
    public function create()
    {
        // Obtém todos os clientes e funcionários para serem utilizados no formulário
        $clientes = Cliente::all();
        $funcionarios = Funcionario::all();

        // Retorna a view 'locacao.consultar' com os clientes e funcionários para o formulário
        return view('locacao.consultar', compact('clientes', 'funcionarios'));
    }

    // Método para exibir a view de cadastro de locações
    public function createCadastro()
    {
        // Obtém todos os veículos, funcionários e clientes para serem utilizados no formulário
        $veiculos = Veiculo::all();
        $funcionarios = Funcionario::all();
        $clientes = Cliente::all();

        // Retorna a view 'locacao.cadastro' com veículos, funcionários e clientes para o formulário
        return view('locacao.cadastro', compact('veiculos', 'funcionarios', 'clientes'));
    }
    
    // Método para cadastrar uma nova locação no banco de dados
    public function cadastrarLocacao(Request $request)
    {
        $locacao = new Locacao();

        // Atribui valores aos campos da locação com base nos dados do formulário
        $locacao->id_veiculo = $request->id_veiculo;
        $locacao->id_cliente = $request->id_cliente;
        $locacao->id_funcionario = $request->id_funcionario;
        $locacao->data_saida = $request->data_saida;
        $locacao->data_devolucao = $request->data_devolucao;
        $locacao->quilometragem_saida = $request->quilometragem_saida;
        $locacao->quilometragem_devolucao = $request->quilometragem_devolucao;
        $locacao->qtde_diaria = $request->qtde_diaria;
        $locacao->valor_locacao = $request->valor_locacao;
        $locacao->data_cadastro = date('Y-m-d H:i:s');

        // Salva a nova locação no banco de dados
        $locacao->save();

        // Redireciona para a página de consulta com mensagem de sucesso
        return redirect(route('locacao.view-menu'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }

    // Método para consultar locações com base nos parâmetros do formulário
    public function consultarLocacao()
    {
        // Obtém os parâmetros de consulta do formulário
        $id_cliente = request('id_cliente');
        $id_funcionario = request('id_funcionario');
        $data_retirada = request('data_retirada');
        $data_devolucao = request('data_devolucao');

        // Obtém todos os clientes e funcionários para serem utilizados no formulário
        $clientes = Cliente::all();
        $funcionarios = Funcionario::all();

        // Chama um método estático no modelo Locacao para obter as locações com base nos parâmetros
        $locacoes = Locacao::getLocacoes($id_cliente, $id_funcionario, $data_retirada, $data_devolucao);

        // Retorna a view 'locacao.consultar' com as locações e dados dos clientes e funcionários para o formulário
        return view('locacao.consultar', compact('locacoes', 'clientes', 'funcionarios'));
    }

    // Método para exibir a view de edição de uma locação específica
    public function editarLocacao($id_locacao)
    {
        // Obtém todos os veículos, funcionários e clientes para serem utilizados no formulário
        $veiculos = Veiculo::all();
        $funcionarios = Funcionario::all();
        $clientes = Cliente::all();

        // Busca a locação específica pelo ID
        $locacao = Locacao::findOrFail($id_locacao);

        // Retorna a view 'locacao.editar' com a locação e dados de veículos, funcionários e clientes para o formulário
        return view('locacao.editar', compact('locacao', 'veiculos', 'funcionarios', 'clientes'));
    }

    // Método para atualizar os dados de uma locação no banco de dados
    public function atualizarLocacao(Request $request) 
    {
        // Obtém todos os dados do formulário
        $locacao = $request->all();

        // Atualiza a locação no banco de dados com base no ID
        Locacao::findOrFail($request->id_locacao)->update($locacao);

        // Redireciona para a página de consulta após a atualização com mensagem de sucesso
        return redirect(route('locacao.consultar'))->with('alertaSucesso', 'Cadastro atualizado com sucesso!');
    }

    // Método para excluir uma locação do banco de dados
    public function deletarLocacao($id_locacao)
    {
        // Encontra e exclui a locação específica pelo ID
        Locacao::findOrFail($id_locacao)->delete();
        
        // Redireciona para a página de consulta após a exclusão com mensagem de sucesso
        return redirect(route('locacao.consultar'))->with('alertaSucesso', 'Cadastro excluído com sucesso!');
    }
}
