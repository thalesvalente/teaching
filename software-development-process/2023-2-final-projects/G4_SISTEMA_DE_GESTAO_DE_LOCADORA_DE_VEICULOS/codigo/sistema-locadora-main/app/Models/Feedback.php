<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Feedback extends Model
{
    use HasFactory;

    // Define o nome da tabela no banco de dados associada a este modelo
    protected $table = 'feedback';

    // Define a chave primária da tabela
    protected $primaryKey = 'id_feedback';

    // Define quais atributos não podem ser atribuídos em massa (mass-assignment)
    protected $guarded = [];

    // Desativa a criação automática de timestamps (created_at e updated_at)
    public $timestamps = false;
}

