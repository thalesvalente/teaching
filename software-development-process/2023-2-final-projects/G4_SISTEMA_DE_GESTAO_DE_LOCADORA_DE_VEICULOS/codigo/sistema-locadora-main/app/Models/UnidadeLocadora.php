<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class UnidadeLocadora extends Model
{
    use HasFactory;

    protected $table = 'unidade_locadora';
    protected $primaryKey = 'id_unidade_locadora';
    protected $guarded = [];
    public $timestamps = false;

    //Método para retornar todos os registros e informações da tabela unidade_locadora.
    public static function getAllUnidades($cidade, $estado, $id_unidade_locadora)
    {
        $query = self::select('unidade_locadora.*');
    
        // Adiciona condição para cidade ou estado se não for vazio
        if (!empty($cidade)) {
            $query->where('unidade_locadora.cidade', 'like', '%' . $cidade . '%');
        }
    
        if (!empty($estado)) {
            $query->orWhere('unidade_locadora.estado', 'like', '%' . $estado . '%');
        }
    
        // Adiciona condição para id_unidade_locadora se não for vazio
        if (!empty($id_unidade_locadora)) {
            $query->where('unidade_locadora.id_unidade_locadora', '=', $id_unidade_locadora);
        }
    
        $result = $query->get();

        return $result;
    }
    
    
}
