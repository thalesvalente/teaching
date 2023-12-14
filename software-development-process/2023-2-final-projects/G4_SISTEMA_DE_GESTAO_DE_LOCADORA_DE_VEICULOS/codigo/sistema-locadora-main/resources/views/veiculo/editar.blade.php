@extends('dashboard_main')

@section('content')

    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center">
        <h2 class="mb-0"><i class="bi bi-person-fill me-2"></i>Veiculos - Editar Cadastro</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('veiculo.consultar') }}" class="btn btn-danger" id="btnVoltar"><i class="bi bi-arrow-left-circle-fill"></i>Voltar</a>
            <a href="{{ route('veiculo.cadastro') }}" class="btn btn-success" id="btnNovoCliente"><i class="bi bi-car-front"></i>Novo Veículo</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('veiculo.atualizar', ['id_veiculo' => $veiculo->id_veiculo]) }}" method="POST" enctype="multipart/form-data">
            @csrf
            @method('PUT')
            <div class="mb-3 row">
                <div class="col-md-6 mb-3">
                    <label for="nome" class="form-label col-md-2">Nome</label>
                    <input type="text" class="form-control" id="nome" name="nome" value="{{ $veiculo->nome }}" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="placa" class="form-label col-md-2">Placa</label>
                    <input type="text" class="form-control" id="placa" name="placa" value="{{ $veiculo->placa }}" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="modelo" class="form-label col-md-2">Modelo</label>
                    <select class="form-select" id="modelo" name="modelo">
                        <option value="">Selecione o modelo do veículo</option>
                        <option value="Sedan" <?= $veiculo->modelo == "Sedan" ? "" : "selected"?> >Sedan</option>
                        <option value="Hatch" <?= $veiculo->modelo == "Hatch" ? "" : "selected"?>>Hatch</option>
                        <option value="SUV" <?= $veiculo->modelo == "SUV" ? "" : "selected"?>>SUV</option>
                        <option value="Utilitário" <?= $veiculo->modelo == "Utilitário" ? "" : "selected"?>>Utilitário</option>
                        <option value="Caminhonete" <?= $veiculo->modelo == "Caminhonete" ? "" : "selected"?>>Caminhonete</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="marca" class="form-label col-md-2">Marca</label>
                    <select class="form-select" id="marca" name="marca">
                        <option value="">Selecione a marca do veículo</option>
                        <option value="Chevrolett"  <?= $veiculo->marca == "Sedan" ? "" : "selected"?>>Chevrolett</option>
                        <option value="Toyota" <?= $veiculo->marca == "Toyota" ? "" : "selected"?>>Toyota</option>
                        <option value="Hyundai" <?= $veiculo->marca == "Hyundai" ? "" : "selected"?>>Hyundai</option>
                        <option value="Volvo" <?= $veiculo->marca == "Volvo" ? "" : "selected"?>>Volvo</option>
                        <option value="Ford" <?= $veiculo->marca == "Ford" ? "" : "selected"?>>Ford</option>
                        <option value="Citroen" <?= $veiculo->marca == "Citroen" ? "" : "selected"?>>Citroen</option>
                        <option value="Renault" <?= $veiculo->marca == "Renault" ? "" : "selected"?>>Renault</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="ano" class="form-label col-md-2">Ano</label>
                    <input type="text" class="form-control" id="ano" name="ano" value="{{ $veiculo->ano }}" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="quilometragem" class="form-label col-md-2">Quilometragem</label>
                    <input type="number" class="form-control" id="quilometragem" name="quilometragem" value="{{ $veiculo->quilometragem }}" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="id_unidade_locadora" class="form-label col-md-2">Unidade</label>
                    <select class="form-select" id="id_unidade_locadora" name="id_unidade_locadora">
                        <option value="">Selecione a locadora do veículo</option>
                        @foreach ($unidadesLocadora as $unidadeLocadora) 
                            <option value={{ $unidadeLocadora->id_unidade_locadora }} <?= $veiculo->id_veiculo == $unidadeLocadora->id_veiculo ? "selected" : "" ?>> {{ $unidadeLocadora->cidade . ' - ' . $unidadeLocadora->id_unidade_locadora  }}</option>
                        @endforeach
                    </select>
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Atualizar</button>
            </div>
        </form>
    </div>

@endsection