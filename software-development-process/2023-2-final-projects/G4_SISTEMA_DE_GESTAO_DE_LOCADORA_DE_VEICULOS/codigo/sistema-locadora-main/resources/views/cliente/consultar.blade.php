@extends('dashboard_main')

@section('content')
    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center text-center">
        <h2 class="mb-0"><i class="bi bi-person-fill me-2"></i>Clientes</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('cliente.cadastro') }}" class="btn btn-success" id="btnNovoCliente"><i class="bi bi-person-fill-add"></i>Novo Cliente</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('cliente.consultar') }}" method="GET" enctype="multipart/form-data">
            @csrf
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="nome" class="form-label col-md-2">Nome</label>
                    <input type="text" class="form-control" id="nome" name="nome">
                </div>
                <div class="col-md-6">
                    <label for="cpf" class="form-label col-md-2">CPF</label>
                    <input type="text" class="form-control" id="cpf" name="cpf">
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Consultar</button>
            </div>
        </form>
    </div>

    @if( isset($clientes) )

    <div class="info-section bg-body-tertiary">
        <h2><i class="bi bi-search me-2"></i>Consulta de Clientes</h2>
    </div>

    @if(count($clientes) == 0)
        <div class="alert alert-warning" role="alert">
            <i class="bi bi-exclamation-triangle-fill"></i> Não há nenhum registro de cliente na base de dados!
        </div>
    @endif

    <table class="table">
        <thead class="bg-tertiary">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Nome</th>
                <th scope="col">CPF</th>
                <th scope="col">Telefone</th>
                <th scope="col">Data Cadastro</th>
                <th scope="col">Ações</th>
            </tr>
        </thead>
        <tbody>
            @foreach($clientes as $cliente)
            <tr>
                <th scope="row">{{$cliente->id_cliente}}</th>
                <td>{{$cliente->nome}}</td>
                <td>{{$cliente->cpf}}</td>
                <td>{{$cliente->telefone}}</td>
                <td>{{date('d/m/Y', strtotime($cliente->data_cadastro))}}</td>
                <td class="d-flex gap-2">
                    <a href="{{ route('cliente.editar', $cliente->id_cliente) }}" class="btn btn-secondary acoes" title="Editar">
                       <i class="bi bi-pen"></i>
                    </a>
                    <form action="{{ route('cliente.deletar', $cliente->id_cliente) }}" method="POST">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="btn btn-danger acoes" title="Deletar"><i class="bi bi-trash3"></i></button>
                    </form>
                </td>

            </tr>
            @endforeach
        </tbody>
    </table>
    @endif

    @if (session('alertaSucesso'))

        @include('components.alerta_sucesso')

    @endif

@endsection