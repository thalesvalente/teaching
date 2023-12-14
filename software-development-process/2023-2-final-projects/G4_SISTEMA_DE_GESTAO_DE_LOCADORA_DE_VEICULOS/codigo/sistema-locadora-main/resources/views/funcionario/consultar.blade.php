@extends('dashboard_main')

@section('content')
    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center text-center">
        <h2 class="mb-0"><i class="bi bi-person-fill me-2"></i>Funcionários</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('funcionario.cadastro') }}" class="btn btn-success" id="btnNovofuncionario"><i class="bi bi-person-fill-add"></i>Novo Funcionário</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('funcionario.consultar') }}" method="GET" enctype="multipart/form-data">
            @csrf
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="nome" class="form-label col-md-2">Nome</label>
                    <input type="text" class="form-control" id="nome" name="nome" >
                </div>
                <div class="col-md-6 mb-3">
                    <label for="cargo" class="form-label col-md-2">Cargo</label>
                    <select class="form-select" id="cargo" name="id_cargo">
                        <option value="">Selecione o cargo</option>
                        <option value="1">Gerente</option>
                        <option value="2">Atendente</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="id_unidade_locadora" class="form-label col-md-2">Unidade</label>
                    <select class="form-select" id="id_unidade_locadora" name="id_unidade_locadora">
                        <option  value="">Selecione a unidade</option>
                        @foreach ($unidadesLocadora as $unidadeLocadora)
                            <option value={{ $unidadeLocadora->id_unidade_locadora }}> {{ $unidadeLocadora->cidade . ' - ' . $unidadeLocadora->id_unidade_locadora  }}</option>
                        @endforeach
                    </select>
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Consultar</button>
            </div>
        </form>
    </div>

    @if( isset($funcionarios) )

    <div class="info-section bg-body-tertiary">
        <h2><i class="bi bi-search me-2"></i>Consulta de Funcionários</h2>
    </div>

    @if(count($funcionarios) == 0)
        <div class="alert alert-warning" role="alert">
            <i class="bi bi-exclamation-triangle-fill"></i> Não há nenhum registro de funcionário na base de dados!
        </div>
    @endif

    <table class="table">
        <thead class="bg-tertiary">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Nome</th>
                <th scope="col">Cargo</th>
                <th scope="col">Unidade</th>
                <th scope="col">Data Cadastro</th>
                <th scope="col">Ações</th>
            </tr>
        </thead>
        <tbody>
            @foreach($funcionarios as $funcionario)
            <tr>
                <th scope="row">{{$funcionario->id_funcionario}}</th>
                <td>{{$funcionario->nome}}</td>
                <td>{{$funcionario->id_cargo}}</td>
                <td>{{$funcionario->cidade . ' - ' . $funcionario->id_unidade_locadora}}</td>
                <td>{{date('d/m/Y', strtotime($funcionario->data_cadastro))}}</td>
                <td class="d-flex gap-2">
                    <a href="{{ route('funcionario.editar', $funcionario->id_funcionario) }}" class="btn btn-secondary acoes" title="Editar">
                       <i class="bi bi-pen"></i>
                    </a>
                    <form action="{{ route('funcionario.deletar', $funcionario->id_funcionario) }}" method="POST">
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