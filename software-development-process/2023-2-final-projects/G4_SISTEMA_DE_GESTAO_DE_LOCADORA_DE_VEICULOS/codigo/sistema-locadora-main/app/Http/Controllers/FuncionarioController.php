<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Funcionario;
use App\Models\UnidadeLocadora;

class FuncionarioController extends Controller
{
    //Método responsável por carregar a View de Consulta do módulo Funcionário.
    public function create()
    {
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado = null, $id_unidade_locadora = null );
        return view('funcionario.consultar', compact('unidadesLocadora'));
    }

    //Método responsável por carregar a View de Cadastro do módulo Funcinário.
    public function createCadastro()
    {
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado = null, $id_unidade_locadora = null );
        return view('funcionario.cadastro', compact('unidadesLocadora'));
    }

    //Método responsável por realizar ação de cadastro de dados do módulo Funcionário.
    public function cadastrarFuncionario(Request $request)
    {
        $funcionario = new Funcionario();

        //$funcionario->id_funcionario = $request->id_funcionario;
        $funcionario->id_unidade_locadora = $request->id_unidade_locadora;
        $funcionario->id_cargo = $request->id_cargo;
        $funcionario->nome = $request->nome;
        $funcionario->data_cadastro = date('Y-m-d H:i:s');

        $funcionario->save();

        return redirect(route('funcionario.view-menu'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }

    //Método responsável por realizar ação de consulta de dados do módulo Funcionário.
    public function consultarFuncionario()
    {

        $nome_funcionario = request('nome');
        $id_cargo = request('id_cargo');
        $id_unidade_locadora = request('id_unidade_locadora');
        
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado = null, $id_unidade_locadora);
        $funcionarios = Funcionario::getFuncionarioJoinUnidadeLocadora($nome_funcionario, $id_cargo, $id_unidade_locadora);
        return view('funcionario.consultar', compact('funcionarios',  'unidadesLocadora'));
    }
    
    //Método responsável por carregar a View de Edição do módulo Funcionário.
    public function editarFuncionario($id_funcionario) {
        $funcionario = Funcionario::findOrFail($id_funcionario);
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado = null, $id_unidade_locadora = null );
        return view('funcionario.editar', compact('funcionario', 'unidadesLocadora'));
    }

    //Método responsável por realizar ação de atualização de dados do módulo Funcionário.
    public function atualizarFuncionario(Request $request) 
    {
        $funcionario = $request->all();
        Funcionario::findOrFail($request->id_funcionario)->update($funcionario);
        return redirect(route('funcionario.consultar'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }

    //Método responsável por realizar ação de exclusão de dados do módulo Funcionário.
    public function deletarFuncionario($id_funcionario)
    {
        Funcionario::findOrFail($id_funcionario)->delete();
        return redirect(route('funcionario.consultar'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }
}
