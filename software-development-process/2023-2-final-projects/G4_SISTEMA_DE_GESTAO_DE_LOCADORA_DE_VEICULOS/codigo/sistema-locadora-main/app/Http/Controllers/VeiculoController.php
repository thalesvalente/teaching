<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Veiculo;
use App\Models\UnidadeLocadora;

class VeiculoController extends Controller
{
    // Método para exibir a view de consulta de veículos
    public function create(){
        // Obtém todas as unidades locadoras para serem utilizadas no formulário
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado  = null, $id_unidade_locadora = null);

        // Retorna a view 'veiculo.consultar' com as unidades locadoras para o formulário
        return view('veiculo.consultar', compact('unidadesLocadora'));
    }

    // Método para exibir a view de cadastro de veículos
    public function createCadastro(){
        // Obtém todas as unidades locadoras para serem utilizadas no formulário
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado  = null, $id_unidade_locadora = null);

        // Retorna a view 'veiculo.cadastro' com as unidades locadoras para o formulário
        return view('veiculo.cadastro', compact('unidadesLocadora'));
    }

    // Método para cadastrar um novo veículo no banco de dados
    public function cadastrarVeiculo(Request $request)
    {
        $veiculo = new Veiculo();

        // Atribui valores aos campos do veículo com base nos dados do formulário
        $veiculo->id_unidade_locadora = $request->id_unidade_locadora;
        $veiculo->placa = $request->placa;
        $veiculo->nome = $request->nome;
        $veiculo->modelo = $request->modelo;
        $veiculo->marca = $request->marca;
        $veiculo->ano = $request->ano;
        $veiculo->quilometragem = $request->quilometragem;
        $veiculo->data_cadastro =  date('Y-m-d H:i:s');
                
        // Salva o novo veículo no banco de dados
        $veiculo->save();

        // Redireciona para a página de consulta com mensagem de sucesso
        return redirect(route('veiculo.view-menu'))->with('alertaSucesso', 'Cadastro realizado com sucesso!');
    }

    // Método para consultar todos os veículos no banco de dados
    public function consultarVeiculo()
    {
        // Obtém todos os veículos e unidades locadoras para serem utilizados no formulário
        $veiculos = Veiculo::all();
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado  = null, $id_unidade_locadora = null);

        // Retorna a view 'veiculo.consultar' com os veículos e unidades locadoras para o formulário
        return view('veiculo.consultar', compact('veiculos', 'unidadesLocadora'));
    }

    // Método para exibir a view de edição de um veículo específico
    public function editarVeiculo($id_veiculo) {
        // Obtém todas as unidades locadoras para serem utilizadas no formulário
        $unidadesLocadora = UnidadeLocadora::getAllUnidades($cidade = null, $estado  = null, $id_unidade_locadora = null);

        // Busca o veículo específico pelo ID
        $veiculo = Veiculo::findOrFail($id_veiculo);

        // Retorna a view 'veiculo.editar' com o veículo e unidades locadoras para o formulário
        return view('veiculo.editar', compact('veiculo', 'unidadesLocadora'));
    }

    // Método para atualizar os dados de um veículo no banco de dados
    public function atualizarVeiculo(Request $request) 
    {
        // Obtém todos os dados do formulário
        $veiculo = $request->all();

        // Atualiza o veículo no banco de dados com base no ID
        Veiculo::findOrFail($request->id_veiculo)->update($veiculo);

        // Redireciona para a página de consulta após a atualização com mensagem de sucesso
        return redirect(route('veiculo.consultar'))->with('alertaSucesso', 'Cadastro atualizado com sucesso!');
    }

    // Método para excluir um veículo do banco de dados
    public function deletarVeiculo($id_veiculo)
    {
        // Encontra e exclui o veículo específico pelo ID
        Veiculo::findOrFail($id_veiculo)->delete();
        
        // Redireciona para a página de consulta após a exclusão com mensagem de sucesso
        return redirect(route('veiculo.consultar'))->with('alertaSucesso', 'Cadastro atualizado com sucesso!');
    }
}
