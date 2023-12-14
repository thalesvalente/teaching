<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('locacao', function (Blueprint $table) {
            $table->bigIncrements('id_locacao');
            $table->integer('id_veiculo');
            $table->integer('id_cliente');
            $table->integer('id_funcionario');
            $table->date('data_saida');
            $table->date('data_devolucao')->nullable();
            $table->integer('quilometragem_saida');
            $table->integer('quilometragem_devolucao')->nullable();;
            $table->integer('qtde_diaria')->nullable();
            $table->integer('valor_locacao')->nullable();
            $table->date('data_cadastro');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('locacao');
    }
};
