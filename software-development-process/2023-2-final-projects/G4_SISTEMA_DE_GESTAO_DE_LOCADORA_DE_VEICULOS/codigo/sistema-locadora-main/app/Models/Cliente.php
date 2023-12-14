<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Cliente extends Model
{
    use HasFactory;

    // Define o nome da tabela no banco de dados associada a este modelo
    protected $table = 'cliente';

    // Define a chave primária da tabela
    protected $primaryKey = 'id_cliente';

    // Define quais atributos não podem ser atribuídos em massa (mass-assignment)
    protected $guarded = [];

    // Desativa a criação automática de timestamps (created_at e updated_at)
    public $timestamps = false;

    // Método estático para obter clientes com base no nome e/ou CPF
    public static function getClientesByNomeCpf($nome, $cpf)
    {
        // Cria uma instância da query usando o próprio modelo
        $query = self::select('cliente.*');

        // Adiciona condição para nome do cliente se não for vazio
        if (!empty($nome)) {
            $query->where('cliente.nome', 'like', '%' . $nome . '%');
        }

        // Adiciona condição para CPF do cliente se não for vazio
        if (!empty($cpf)) {
            $query->orWhere('cliente.cpf', 'like', '%' . $cpf . '%');
        }

        // Executa a query e obtém os resultados
        $result = $query->get();

        // Retorna os resultados
        return $result;
    }
}

