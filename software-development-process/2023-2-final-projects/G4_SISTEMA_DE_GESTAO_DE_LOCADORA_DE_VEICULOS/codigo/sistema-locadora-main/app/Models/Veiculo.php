<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Veiculo extends Model
{
    use HasFactory;

    protected $table = 'veiculo';
    protected $primaryKey = 'id_veiculo';
    protected $guarded = [];  
    public $timestamps = false;
    
    //Método para retornar todos os registros e informações de veiculos que que estão registrados em Unidade.
    public static function getVeiculoJoinUnidadeLocadora($id_veiculo, $id_unidade_locadora)
    {

        $query = self::select('veiculo.*', 'unidade_locadora.cidade', 'unidade_locadora.id_unidade_locadora')
            ->join('unidade_locadora', 'veiculo.id_unidade_locadora', '=', 'unidade_locadora.id_unidade_locadora');
    
        // Adiciona condição para id_veiculo se não for vazio
        if (!empty($id_veiculo)) {
            $query->where('veiculo.id_veiculo', '=', $id_veiculo);
        }
    
        // Adiciona condição para ID da unidade locadora se não for vazio
        if (!empty($id_unidade_locadora)) {
            $query->where('unidade_locadora.id_unidade_locadora', '=', $id_unidade_locadora);
        }
    
        $result = $query->get();
    
        return $result;
    }
}
