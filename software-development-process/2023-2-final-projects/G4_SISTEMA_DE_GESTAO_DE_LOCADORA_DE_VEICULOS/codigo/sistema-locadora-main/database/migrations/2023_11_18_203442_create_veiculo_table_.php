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
        Schema::create('veiculo', function (Blueprint $table) {
            $table->bigIncrements('id_veiculo');
            $table->integer('id_unidade_locadora');
            $table->string('placa', 20);
            $table->string('nome', 100);
            $table->string('modelo', 50);
            $table->string('marca', 50);
            $table->string('ano', 50);
            $table->integer('quilometragem');
            $table->date('data_cadastro');
            $table->string('image')->nullable();
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
        Schema::dropIfExists('veiculo');
    }
};
