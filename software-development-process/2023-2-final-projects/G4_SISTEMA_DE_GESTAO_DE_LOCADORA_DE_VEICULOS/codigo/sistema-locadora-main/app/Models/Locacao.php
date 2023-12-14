<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Locacao extends Model
{
    use HasFactory;

    protected $table = 'locacao';
    protected $primaryKey = 'id_locacao';
    protected $guarded = [];  
    public $timestamps = false;

    /**
     * Obtém registros da tabela 'locacao' com base nos parâmetros fornecidos.
     *
     * @param int|null    $id_cliente      ID do cliente.
     * @param int|null    $id_funcionario  ID do funcionário.
     * @param string|null $data_retirada    Data de retirada (opcional, compara com a data atual se não fornecida).
     * @param string|null $data_devolucao   Data de devolução (opcional, compara com a data atual se não fornecida).
     *
     * @return \Illuminate\Database\Eloquent\Collection Lista de registros da tabela 'locacao' que correspondem aos critérios.
     */
    public static function getLocacoes($id_cliente, $id_funcionario, $data_retirada, $data_devolucao)
    {
        $query = self::select('locacao.*');

        // Adiciona condição para ID do cliente se não for vazio
        if (!empty($id_cliente)) {
            $query->where('locacao.id_cliente', '=', $id_cliente);
        }

        // Adiciona condição para ID do funcionário se não for vazio
        if (!empty($id_funcionario)) {
            $query->where('locacao.id_funcionario', '=', $id_funcionario);
        }

        // Adiciona condição para data de retirada se ambas as datas são fornecidas ou compara com a data atual se não for fornecida
        if (!empty($data_retirada) && empty($data_devolucao)) {
            $query->where('locacao.data_retirada', '=', $data_retirada);
        }

        // Adiciona condição para data de devolução se ambas as datas são fornecidas ou compara com a data atual se não for fornecida
        if (!empty($data_devolucao) && empty($data_retirada)) {
            $query->where('locacao.data_devolucao', '=', $data_devolucao);
        }

        // Adiciona condição para ambas as datas usando BETWEEN se ambas são fornecidas
        if (!empty($data_retirada) && !empty($data_devolucao)) {
            $query->whereBetween('locacao.data_retirada', [$data_retirada, $data_devolucao]);
        }

        $result = $query->get();

        return $result;
    }
}
