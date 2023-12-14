<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Cliente;

class ClienteController extends Controller
{
    // Método para exibir a view de consulta de clientes
    public function create(){
        return view('cliente.consultar');
    }

    // Método para exibir a view de cadastro de clientes
    public function createCadastro(){
        return view('cliente.cadastro');
    }
    
    // Método para cadastrar um novo cliente no banco de dados
    public function cadastrarCliente(Request $request)
    {
        $cliente = new Cliente();

        // Atribui valores aos campos do cliente com base nos dados do formulário
        $cliente->nome = $request->nome;
        $cliente->cpf = $request->cpf;
        $cliente->endereco = $request->endereco;
        $cliente->telefone = $request->telefone;
        $cliente->data_cadastro = date('Y-m-d H:i:s');

        // Salva o novo cliente no banco de dados
        $cliente->save();

        // Redireciona para a página de consulta com mensagem de sucesso
        return redirect(route('cliente.view-menu'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }

    // Método para consultar clientes com base no nome e/ou CPF
    public function consultarCliente()
    {
        // Obtém os parâmetros de consulta do formulário
        $nome_cliente = request('nome');
        $cpf = request('cpf');

        // Chama um método estático no modelo Cliente para obter os clientes com base nos parâmetros
        $clientes = Cliente::getClientesByNomeCpf($nome_cliente, $cpf);

        // Retorna a view 'cliente.consultar' com a lista de clientes para exibição
        return view('cliente.consultar', compact('clientes'));
    }

    // Método para exibir a view de edição de um cliente específico
    public function editarCliente($id_cliente) {
        // Busca o cliente específico pelo ID
        $cliente = Cliente::findOrFail($id_cliente);

        // Retorna a view 'cliente.editar' com o cliente a ser editado
        return view('cliente.editar', compact('cliente'));
    }

    // Método para atualizar os dados de um cliente no banco de dados
    public function atualizarCliente(Request $request) 
    {
        // Obtém todos os dados do formulário
        $cliente = $request->all();

        // Atualiza o cliente no banco de dados com base no ID
        Cliente::findOrFail($request->id_cliente)->update($cliente);

        // Redireciona para a página de consulta após a atualização com mensagem de sucesso
        return redirect(route('cliente.consultar'))->with('alertaSucesso', 'Cadastro atualizado com sucesso!');
    }

    // Método para excluir um cliente do banco de dados
    public function deletarCliente($id_cliente)
    {
        // Encontra e exclui o cliente específico pelo ID
        Cliente::findOrFail($id_cliente)->delete();
        
        // Redireciona para a página de consulta após a exclusão com mensagem de sucesso
        return redirect(route('cliente.consultar'))->with('alertaSucesso', 'Cadastro excluído com sucesso!');
    }
}
