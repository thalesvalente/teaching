@extends('dashboard_main')

@section('content')
    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center">
        <h2 class="mb-0"><i class="bi bi-car-front-fill me-2"></i>Veículos</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('veiculo.cadastro') }}" class="btn btn-success" id="btnNovoCliente"><i class="bi bi-car-front"></i>Novo Veículo</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('veiculo.consultar') }}" method="GET" enctype="multipart/form-data">
            @csrf
            <div class="mb-3 row">
                <div class="col-md-6 mb-3">
                    <label for="nome" class="form-label col-md-2">Nome</label>
                    <input type="text" class="form-control" id="nome" name="nome">
                </div>
                <div class="col-md-6 mb-3">
                    <label for="placa" class="form-label col-md-2">Placa</label>
                    <input type="text" class="form-control" id="placa" name="placa">
                </div>
                <div class="col-md-6 mb-3">
                    <label for="modelo" class="form-label col-md-2">Modelo</label>
                    <select class="form-select" id="modelo" name="modelo">
                        <option value="">Selecione o modelo do veículo</option>
                        <option value="Sedan">Sedan</option>
                        <option value="Hatch">Hatch</option>
                        <option value="SUV">SUV</option>
                        <option value="Utilitário">Utilitário</option>
                        <option value="Caminhonete">Caminhonete</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="marca" class="form-label col-md-2">Marca</label>
                    <select class="form-select" id="marca" name="marca">
                        <option value="">Selecione a marca do veículo</option>
                        <option value="Chevrolett">Chevrolett</option>
                        <option value="Toyota">Toyota</option>
                        <option value="Hyundai">Hyundai</option>
                        <option value="Volvo">Volvo</option>
                        <option value="Ford">Ford</option>
                        <option value="Citroen">Citroen</option>
                        <option value="Renault">Renault</option>
                    </select>
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Consultar</button>
            </div>
        </form>
    </div>

    @if( isset($veiculos) )

    <div class="info-section bg-body-tertiary">
        <h2><i class="bi bi-search me-2"></i>Consulta de Veículos</h2>
    </div>

    @if(count($veiculos) == 0)
        <div class="alert alert-warning" role="alert">
            <i class="bi bi-exclamation-triangle-fill"></i> Não há nenhum registro de veiculo na base de dados!
        </div>
    @endif

    <table class="table">
        <thead class="bg-tertiary">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Nome</th>
                <th scope="col">Placa</th>
                <th scope="col">Marca</th>
                <th scope="col">Modelo</th>
                <th scope="col">Km</th>
                <th scope="col">Ações</th>
            </tr>
        </thead>
        <tbody>
            @foreach($veiculos as $veiculo)
            <tr>
                <th scope="row">{{$veiculo->id_veiculo}}</th>
                <td>{{$veiculo->nome}}</td>
                <td>{{$veiculo->placa}}</td>
                <td>{{$veiculo->marca}}</td>
                <td>{{$veiculo->modelo}}</td>
                <td>{{$veiculo->quilometragem}}</td>
                <td class="d-flex gap-2">
                    <a href="{{ route('veiculo.editar', $veiculo->id_veiculo) }}" class="btn btn-secondary acoes" title="Editar">
                       <i class="bi bi-pen"></i>
                    </a>
                    <form action="{{ route('veiculo.deletar', $veiculo->id_veiculo) }}" method="POST">
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