@extends('dashboard_main')

@section('content')

    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center">
        <h2 class="mb-0"><i class="bi bi-person-fill me-2"></i>Clientes - Editar Cadastro</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('cliente.consultar') }}" class="btn btn-danger" id="btnVoltar"><i class="bi bi-arrow-left-circle-fill"></i>Voltar</a>
            <a href="{{ route('cliente.cadastro') }}" class="btn btn-success" id="btnNovoCliente"><i class="bi bi-person-fill-add"></i>Novo Cliente</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('cliente.atualizar', ['id_cliente' => $cliente->id_cliente]) }}" method="POST" enctype="multipart/form-data">
            @csrf
            @method('PUT')
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="nome" class="form-label col-md-2">Nome</label>
                    <input type="text" class="form-control" id="nome" name="nome" value="{{ $cliente->nome }}" required>
                </div>
                <div class="col-md-6">
                    <label for="cpf" class="form-label col-md-2">CPF</label>
                    <input type="text" class="form-control" id="cpf" name="cpf" value="{{ $cliente->cpf }}" required>
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="endereco" class="form-label col-md-2">Endereço</label>
                    <input type="text" class="form-control" id="endereco" name="endereco" value="{{ $cliente->endereco }}" required>
                </div>
                <div class="col-md-6">
                    <label for="telefone" class="form-label col-md-2">Telefone</label>
                    <input type="text" class="form-control" id="telefone" name="telefone" value="{{ $cliente->telefone }}" required > 
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Atualizar</button>
            </div>
        </form>
    </div>

@endsection