@extends('dashboard_main')

@section('content')
    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center text-center">
        <h2 class="mb-0"><i class="bi bi-car-front-fill me-2"></i>Locação de Veículos</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('locacao.cadastro') }}" class="btn btn-success" id="btnNovolocacao"><i class="bi bi-car-front"></i>Nova Locação</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('locacao.consultar') }}" method="GET" enctype="multipart/form-data">
            @csrf
            <div class="mb-3 row">
                <div class="col-md-6 mb-4">
                    <label for="id_cliente" class="form-label col-md-2">Cliente</label>
                    <select class="form-select" id="id_cliente" name="id_cliente" >
                        <option value="" >Selecione o Cliente</option>
                        @foreach ($clientes as $cliente )
                            <option value="{{ $cliente->id_cliente}}"> {{ $cliente->nome }}</option>
                        @endforeach
                    </select>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="id_funcionario" class="form-label col-md-4">Responsável da Locação</label>
                    <select class="form-select" id="id_funcionario" name="id_funcionario" >
                        <option value="">Selecione o Funcionário Responsável</option>
                        @foreach ($funcionarios as $funcionario )
                            <option value="{{ $funcionario->id_funcionario}}"> {{ $funcionario->nome}}</option>
                        @endforeach
                    </select>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="data_saida" class="form-label col-md-4">Data da Retirada</label>
                    <input type="date" class="form-control" id="data_saida" name="data_saida" >
                </div>
                <div class="col-md-6 mb-4">
                    <label for="data_devolucao" class="form-label col-md-4">Data da Devolucão</label>
                    <input type="date" class="form-control" id="data_devolucao" name="data_devolucao" >
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Consultar</button>
            </div>
        </form>
    </div>

    @if( isset($locacoes) )

    <div class="info-section bg-body-tertiary">
        <h2><i class="bi bi-search me-2"></i>Consulta de Locações</h2>
    </div>

    @if(count($locacoes) == 0)
        <div class="alert alert-warning" role="alert">
            <i class="bi bi-exclamation-triangle-fill"></i> Não há nenhum registro de locação na base de dados!
        </div>
    @endif

    <table class="table">
        <thead class="bg-tertiary">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Cliente</th>
                <th scope="col">Resp. Locação</th>
                <th scope="col">Data Saída</th>
                <th scope="col">Data Devolucão</th>
                <th scope="col">Ações</th>
            </tr>
        </thead>
        <tbody>
            @foreach($locacoes as $locacao)
            <tr>
                <th scope="row">{{$locacao->id_locacao}}</th>
                <td>{{$locacao->id_cliente}}</td>
                <td>{{$locacao->id_funcionario}}</td>
                <td>{{date('d/m/Y', strtotime($locacao->data_saida))}}</td>
                <td>{{date('d/m/Y', strtotime($locacao->data_devolucao))}}</td>
                <td class="d-flex gap-2">
                    <a href="{{ route('locacao.editar', $locacao->id_locacao) }}" class="btn btn-secondary acoes" title="Editar">
                       <i class="bi bi-pen"></i>
                    </a>
                    <form action="{{ route('locacao.deletar', $locacao->id_locacao) }}" method="POST">
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