<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CLienteController;
use App\Http\Controllers\FuncionarioController;
use App\Http\Controllers\UnidadeLocadoraController;
use App\Http\Controllers\VeiculoController;
use App\Http\Controllers\LocacaoController;
use App\Http\Controllers\FeedbackController;
use App\Http\Controllers\CargoController;
use App\Http\Controllers\DashboardController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


Route::get('/', function () {
    return view('auth.login');   
});


//Rotas de Autenticação de Usuario
Route::middleware(['auth:sanctum', 'verified'])->get('/dashboard', [DashboardController::class, 'create'])->name('dashboard');
Route::middleware(['auth:sanctum', 'logout'])->delete('/dashboard', function() {  return view('auth.login'); });


//Rotas do CRUD Cliente
Route::prefix('dashboard/cliente')->group(function(){
    Route::get('/menu', [ClienteController::class, 'create'])->name('cliente.view-menu')->middleware('auth');
    Route::get('/cadastro', [ClienteController::class, 'createCadastro'])->name('cliente.cadastro')->middleware('auth');
    Route::post('/cadastrar', [ClienteController::class, 'cadastrarCliente'])->name('cliente.cadastrar')->middleware('auth');
    Route::get('/consulta', [ClienteController::class, 'consultarCliente'])->name('cliente.consultar')->middleware('auth');
    Route::get('/editar/{id_cliente?}', [ClienteController::class, 'editarCliente'])->name('cliente.editar')->middleware('auth');
    Route::put('/atualizar/{id_cliente}', [ClienteController::class, 'atualizarCliente'])->name('cliente.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_cliente}', [ClienteController::class, 'deletarCliente'])->name('cliente.deletar')->middleware('auth');
});

//Rotas do CRUD Funcinario
Route::prefix('dashboard/funcionario')->group(function(){
    Route::get('/menu', [FuncionarioController::class, 'create'])->name('funcionario.view-menu')->middleware('auth');
    Route::get('/cadastro', [FuncionarioController::class, 'createCadastro'])->name('funcionario.cadastro')->middleware('auth');
    Route::post('/cadastrar', [FuncionarioController::class, 'cadastrarFuncionario'])->name('funcionario.cadastrar')->middleware('auth');
    Route::get('/consulta', [FuncionarioController::class, 'consultarFuncionario'])->name('funcionario.consultar')->middleware('auth');
    Route::get('/editar/{id_funcionario?}', [FuncionarioController::class, 'editarFuncionario'])->name('funcionario.editar')->middleware('auth');
    Route::put('/atualizar/{id_funcionario}', [FuncionarioController::class, 'atualizarFuncionario'])->name('funcionario.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_funcionario}', [FuncionarioController::class, 'deletarFuncionario'])->name('funcionario.deletar')->middleware('auth');
});


//Rotas do CRUD UnidadeLocadora
Route::prefix('dashboard/unidadeLocadora')->group(function(){
    Route::get('/menu', [UnidadeLocadoraController::class, 'create'])->name('unidadeLocadora.view-menu')->middleware('auth');
    Route::get('/cadastro', [UnidadeLocadoraController::class, 'createCadastro'])->name('unidadeLocadora.cadastro')->middleware('auth');
    Route::post('/cadastrar', [UnidadeLocadoraController::class, 'cadastrarUnidadeLocadora'])->name('unidadeLocadora.cadastrar')->middleware('auth');
    Route::get('/consulta', [UnidadeLocadoraController::class, 'consultarUnidadeLocadora'])->name('unidadeLocadora.consultar')->middleware('auth');
    Route::get('/editar/{id_unidade_locadora?}', [UnidadeLocadoraController::class, 'editarUnidadeLocadora'])->name('unidadeLocadora.editar')->middleware('auth');
    Route::put('/atualizar/{id_unidade_locadora}', [UnidadeLocadoraController::class, 'atualizarUnidadeLocadora'])->name('unidadeLocadora.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_unidade_locadora?}', [UnidadeLocadoraController::class, 'deletarUnidadeLocadora'])->name('unidadeLocadora.deletar')->middleware('auth');
});

//Rotas do CRUD Veiculo
Route::prefix('dashboard/veiculo')->group(function(){
    Route::get('/menu', [VeiculoController::class, 'create'])->name('veiculo.view-menu')->middleware('auth');
    Route::get('/cadastro', [VeiculoController::class, 'createCadastro'])->name('veiculo.cadastro')->middleware('auth');
    Route::post('/cadastrar', [VeiculoController::class, 'cadastrarVeiculo'])->name('veiculo.cadastrar')->middleware('auth');
    Route::get('/consulta', [VeiculoController::class, 'consultarVeiculo'])->name('veiculo.consultar')->middleware('auth');
    Route::get('/editar/{id_veiculo?}', [VeiculoController::class, 'editarVeiculo'])->name('veiculo.editar')->middleware('auth');
    Route::put('/atualizar/{id_veiculo}', [VeiculoController::class, 'atualizarVeiculo'])->name('veiculo.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_veiculo}', [VeiculoController::class, 'deletarVeiculo'])->name('veiculo.deletar')->middleware('auth');
});

//Rotas do CRUD Locacao
Route::prefix('dashboard/locacao')->group(function(){
    Route::get('/menu', [LocacaoController::class, 'create'])->name('locacao.view-menu')->middleware('auth');
    Route::get('/cadastro', [LocacaoController::class, 'createCadastro'])->name('locacao.cadastro')->middleware('auth');
    Route::post('/cadastrar', [LocacaoController::class, 'cadastrarLocacao'])->name('locacao.cadastrar')->middleware('auth');
    Route::get('/consulta', [LocacaoController::class, 'consultarLocacao'])->name('locacao.consultar')->middleware('auth');
    Route::get('/editar/{id_locacao?}', [LocacaoController::class, 'editarLocacao'])->name('locacao.editar')->middleware('auth');
    Route::put('/atualizar/{id_locacao}', [LocacaoController::class, 'atualizarLocacao'])->name('locacao.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_locacao}', [LocacaoController::class, 'deletarLocacao'])->name('locacao.deletar')->middleware('auth');
});

//Rotas do CRUD Feedback
Route::prefix('dashboard/feedback')->group(function(){
    Route::get('/menu', [FeedbackController::class, 'create'])->name('feedback.view-menu')->middleware('auth');
    Route::post('/cadastrar', [FeedbackController::class, 'cadastrarFeedback'])->name('feedback.cadastrar')->middleware('auth');
    Route::get('/consultar', [FeedbackController::class, 'consultarFeedback'])->name('feedback.consultar')->middleware('auth');
    Route::get('/editar/{id_feedback?}', [FeedbackController::class, 'editarFeedback'])->name('feedback.editar')->middleware('auth');
    Route::put('/atualizar/{id_feedback}', [FeedbackController::class, 'atualizarFeedback'])->name('feedback.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_feedback}', [FeedbackController::class, 'deletarFeedback'])->name('feedback.deletar')->middleware('auth');
});

//Rotas do CRUD Cargo
Route::prefix('dashboard/cargo')->group(function(){
    Route::get('/menu', [CargoController::class, 'create'])->name('cargo.view-menu')->middleware('auth');
    Route::post('/cadastrar', [CargoController::class, 'cadastrarCargo'])->name('cargo.cadastrar')->middleware('auth');
    Route::get('/consultar', [CargoController::class, 'consultarCargo'])->name('cargo.consultar')->middleware('auth');
    Route::get('/editar/{id_cargo?}', [CargoController::class, 'editarCargo'])->name('cargo.editar')->middleware('auth');
    Route::put('/atualizar/{id_cargo}', [CargoController::class, 'atualizarCargo'])->name('cargo.atualizar')->middleware('auth');
    Route::delete('/deletar/{id_cargo}', [CargoController::class, 'deletarCargo'])->name('cargo.deletar')->middleware('auth');
});
