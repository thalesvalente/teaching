<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Cargo;

class CargoController extends Controller
{
    // Método para exibir o formulário de cadastro de cargos
    public function create(){
        return view('cargos.cadastrar');
    }
    
    // Método para cadastrar um novo cargo no banco de dados
    public function cadastrarCargo(Request $request)
    {
        $cargo = new Cargo();

        // Atribui valores ao novo cargo com base nos dados do formulário
        $cargo->id_cargo = $request->id_cargo;
        $cargo->data_cadastro = date('d/m/Y H:i');

        // Salva o novo cargo no banco de dados
        $cargo->save();

        // Redireciona de volta para a página de cadastro com mensagem de sucesso
        return redirect('cargos/cadastrar')->with('cadastroRealizado', 'Cadastro realizado com sucesso!');
    }

    // Método para consultar todos os cargos no banco de dados
    public function consultarCargo()
    {
        $cargos = Cargo::all();

        // Retorna a view 'cargos.consultar' com a lista de cargos para exibição
        return view('cargos.consultar', compact('cargos'));
    }

    // Método para exibir o formulário de edição de um cargo específico
    public function editarCargo($id_cargo) {
        // Busca o cargo específico pelo ID
        $cargo = Cargo::findOrFail($id_cargo);

        // Retorna a view 'cargos.editar' com o cargo a ser editado
        return view('cargos.editar', compact('cargo'));
    }

    // Método para atualizar os dados de um cargo no banco de dados
    public function atualizarCargo(Request $request) 
    {
        // Obtém todos os dados do formulário
        $cargo = $request->all();

        // Atualiza o cargo no banco de dados com base no ID
        Cargo::findOrFail($request->id_cargo)->update($cargo);

        // Redireciona para a página de consulta após a atualização
        return redirect('cargos/consultar');
    }

    // Método para excluir um cargo do banco de dados
    public function deletarCargo($id_cargo)
    {
        // Encontra e exclui o cargo específico pelo ID
        Cargo::findOrFail($id_cargo)->delete();
        
        // Redireciona para a página de consulta após a exclusão
        return redirect('cargos/consultar');
    }
}
