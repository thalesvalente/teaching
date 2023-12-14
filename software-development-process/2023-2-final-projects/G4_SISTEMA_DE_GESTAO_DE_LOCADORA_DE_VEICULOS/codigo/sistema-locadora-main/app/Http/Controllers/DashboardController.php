<?php

namespace App\Http\Controllers;

use App\Models\Cliente;
use App\Models\Locacao;
use App\Models\Veiculo;
use Illuminate\Http\Request;

class DashboardController extends Controller
{
    // Método para exibir o dashboard
    public function create(){

        // Obtém a data atual no formato 'd/m/Y'
        $data_atual = date('d/m/Y');

        // Obtém todos os registros de veículos, clientes e locações
        $veiculos = Veiculo::all();
        $clientes = Cliente::all();
        $locacoes = Locacao::all();

        // Calcula o número de veículos, clientes, locações e veículos disponíveis
        $count_veiculos = !empty($veiculos) ? count($veiculos) : 'Sem registros' ;
        $count_clientes = !empty($clientes) ? count($clientes) : 'Sem registros' ;
        $count_locacoes = !empty($locacoes) ? count($locacoes) : 'Sem registros' ;
        $count_veiculos_disponiveis = $count_veiculos - $count_locacoes;

        // Cria um array compacto com as variáveis para serem passadas para a view
        $compact = compact('data_atual', 
                            'count_veiculos',
                            'count_clientes',
                            'count_locacoes',
                            'count_veiculos_disponiveis'
        );

        // Retorna a view 'dashboard' com os dados compactos
        return view('dashboard', $compact);
    }
}

