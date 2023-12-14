<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\UnidadeLocadora;
use App\Models\Funcionario;
class UnidadeLocadoraController extends Controller
{

    //Método responsável por carregar a View de Consulta do módulo Unidades.
    public function create()
    {
        $funcionarios = Funcionario::getAllFuncionarios();
        return view('unidade.consultar', compact('funcionarios'));
    }

    //Método responsável por carregar a View de Cadastro do módulo Unidades.
    public function createCadastro()
    {
       $funcionarios = Funcionario::getAllFuncionarios();
        return view('unidade.cadastro', compact('funcionarios'));
    }

    //Método responsável por realizar ação de cadastro de dados do módulo Unidades.
    public function cadastrarUnidadeLocadora(Request $request)
    {
        $unidadeLocadora = new UnidadeLocadora();

        $unidadeLocadora->cidade = $request->cidade;
        $unidadeLocadora->estado = $request->estado;
        $unidadeLocadora->data_cadastro = date('Y-m-d H:i:s');

        $unidadeLocadora->save();

        return redirect(route('unidadeLocadora.view-menu'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }

    //Método responsável por realizar ação de consulta de dados do módulo Unidades.
    public function consultarUnidadeLocadora()
    {
        $cidade = request('cidade');
        $estado = request('estado');
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade, $estado, $id_unidade_locadora = null);
        $funcionarios = Funcionario::getAllFuncionarios();



        return view('unidade.consultar', compact('unidadesLocadora', 'funcionarios'));
    }

    //Método responsável por carregar a View de Edição do módulo Unidades.
    public function editarUnidadeLocadora($id_unidade_locadora) {
        $unidadeLocadora = UnidadeLocadora::findOrFail($id_unidade_locadora);
        $funcionarios = Funcionario::getFuncionarioJoinUnidadeLocadora($nome_funcionario = null, $id_cargo= null, $id_unidade_locadora = null);
        return view('unidade.editar', compact('unidadeLocadora', 'funcionarios'));
    }

    //Método responsável por realizar ação de atualização de dados do módulo Unidades.
    public function atualizarUnidadeLocadora(Request $request) 
    {
        $unidadeLocadora = $request->all();
        UnidadeLocadora::findOrFail($request->id_unidade_locadora)->update($unidadeLocadora);
        return redirect(route('unidadeLocadora.consultar'))->with('alertaSucesso', 'Cadastro atualizado com sucesso!');
    }

    //Método responsável por realizar ação de exclusão de dados do módulo Unidades.
    public function deletarUnidadeLocadora($id_unidade_locadora)
    {
        UnidadeLocadora::findOrFail($id_unidade_locadora)->delete();
        return redirect(route('unidadeLocadora.consultar'))->with('alertaSucesso', 'Cadastro excluído com sucesso!');
    }
}
