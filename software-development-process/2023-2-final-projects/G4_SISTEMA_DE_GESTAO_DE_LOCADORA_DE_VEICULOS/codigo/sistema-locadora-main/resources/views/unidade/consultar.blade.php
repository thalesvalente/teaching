@extends('dashboard_main')

@section('content')
    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center text-center">
        <h2 class="mb-0"><i class="bi bi-building-fill me-2"></i></i>Unidades da Locadora</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('unidadeLocadora.cadastro') }}" class="btn btn-success" id="btnNovounidadeLocadora"><i class="bi bi-building-fill-add"></i></i>Nova Unidade</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('unidadeLocadora.consultar') }}" method="GET" enctype="multipart/form-data">
            @csrf
            <div class="mb-3 row">
                <div class="col-md-6 mb-3">
                    <label for="cidade" class="form-label col-md-2">Cidade</label>
                    <input type="text" class="form-control" id="cidade" name="cidade" >
                </div>
                <div class="col-md-6 mb-3">
                    <label for="estado" class="form-label col-md-2">Estado</label>
                    <input type="text" class="form-control" id="estado" name="estado" >
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Consultar</button>
            </div>
        </form>
    </div>

    @if( isset($unidadesLocadora) )

    <div class="info-section bg-body-tertiary">
        <h2><i class="bi bi-search me-2"></i>Consulta de Unidades</h2>
    </div>

    @if(count($unidadesLocadora) == 0)
        <div class="alert alert-warning" role="alert">
            <i class="bi bi-exclamation-triangle-fill"></i> Não há nenhum registro de unidades na base de dados!
        </div>
    @endif

    <table class="table">
        <thead class="bg-tertiary">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Cidade</th>
                <th scope="col">Estado</th>
                <th scope="col">Data Cadastro</th>
                <th scope="col">Ações</th>
            </tr>
        </thead>
        <tbody>
            @foreach($unidadesLocadora as $unidadeLocadora)
            <tr>
                <th scope="row">{{$unidadeLocadora->id_unidade_locadora}}</th>
                <td>{{$unidadeLocadora->cidade}}</td>
                <td>{{$unidadeLocadora->estado}}</td>
                <td>{{date('d/m/Y', strtotime($unidadeLocadora->data_cadastro))}}</td>
                <td class="d-flex gap-2">
                    <a href="{{ route('unidadeLocadora.editar', $unidadeLocadora->id_unidade_locadora) }}" class="btn btn-secondary acoes" title="Editar">
                       <i class="bi bi-pen"></i>
                    </a>
                    <form action="{{ route('unidadeLocadora.deletar', $unidadeLocadora->id_unidade_locadora) }}" method="POST">
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