@extends('dashboard_main')

@section('content')

    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center">
        <h2 class="mb-0"><i class="bi bi-person-fill me-2"></i>Locação de Veiculos - Editar Locação</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('locacao.consultar') }}" class="btn btn-danger" id="btnVoltar"><i class="bi bi-arrow-left-circle-fill"></i>Voltar</a>
            <a href="{{ route('locacao.cadastro') }}" class="btn btn-success" id="btnNovoCliente"><i class="bi bi-car-front"></i>Nova Locação</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('locacao.atualizar', ['id_locacao' => $locacao->id_locacao]) }}" method="POST" enctype="multipart/form-data">
            @csrf
            @method('PUT')
            <div class="mb-3 row">
                <div class="col-md-6 mb-4">
                    <label for="id_cliente" class="form-label col-md-2">Cliente</label>
                    <select class="form-select" id="id_cliente" name="id_cliente" required>
                        <option value="">Selecione o Cliente</option>
                        @foreach ($clientes as $cliente )
                            <option value="{{ $cliente->id_cliente}}" <?= $locacao->id_cliente == $cliente->id_cliente ? 'selected' : ""?>> {{ $cliente->nome }}</option>
                        @endforeach
                    </select>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="id_veiculo" class="form-label col-md-2">Veículo</label>
                    <select class="form-select" id="id_veiculo" name="id_veiculo" required>
                        <option value="">Selecione o Veiculo</option>
                        @foreach ($veiculos as $veiculo )
                            <option value="{{ $veiculo->id_veiculo}}" <?= $locacao->id_veiculo == $veiculo->id_veiculo ? 'selected' : ""?>> {{ $veiculo->nome .' ['. $veiculo->placa .'] ' }}</option>
                        @endforeach
                    </select>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="id_funcionario" class="form-label col-md-4">Responsável da Locação</label>
                    <select class="form-select" id="id_funcionario" name="id_funcionario" required>
                        <option >Selecione o Responsável</option>
                        @foreach ($funcionarios as $funcionario )
                            <option value="{{ $funcionario->id_funcionario}}" <?= $locacao->id_funcionario == $funcionario->id_funcionario ? 'selected' : ""?>> {{ $funcionario->nome}}</option>
                        @endforeach
                    </select>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="data_saida" class="form-label col-md-4">Data da Retirada</label>
                    <input type="date" class="form-control" id="data_saida" name="data_saida" value="{{ $locacao->data_saida }}" required>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="data_devolucao" class="form-label col-md-4">Data da Devolucão</label>
                    <input type="date" class="form-control" id="data_devolucao" name="data_devolucao" value="{{ $locacao->data_devolucao }}" required>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="quilometragem_saida" class="form-label col-md-4">Quilometragem de Saída</label>
                    <input type="number" class="form-control" id="quilometragem_saida" name="quilometragem_saida" value="{{ $locacao->quilometragem_saida }}" required>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="quilometragem_devolucao" class="form-label col-md-5">Quilometragem de Devolução</label>
                    <input type="number" class="form-control" id="quilometragem_devolucao" name="quilometragem_devolucao"  value="{{ $locacao->quilometragem_devolucao }}" required>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="qtde_diaria" class="form-label col-md-4">Quantidade de Diárias</label>
                    <input type="number" class="form-control" id="qtde_diaria" name="qtde_diaria"  value="{{ $locacao->qtde_diaria }}" required>
                </div>
                <div class="col-md-6 mb-4">
                    <label for="valor_locacao" class="form-label col-md-4">Valor da Locação</label>
                    <input type="number" class="form-control" id="valor_locacao" name="valor_locacao"  value="{{ $locacao->valor_locacao }}" required>
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Atualizar</button>
            </div>
        </form>
    </div>

@endsection