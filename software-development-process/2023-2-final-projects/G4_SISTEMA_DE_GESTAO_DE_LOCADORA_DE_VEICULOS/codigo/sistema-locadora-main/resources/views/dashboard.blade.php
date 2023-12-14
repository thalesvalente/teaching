@extends('dashboard_main')

@section('content')
    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center">
        <h2 class="mb-0"><i class="bi bi-house-fill me-2"></i>Dashboard</h2>
        <div class="d-flex gap-2">
            <h2 class="mb-0"><i class="bi bi-calendar me-2"></i>{{ $data_atual }}</h2>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
            <div class="container mt-4">
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title"><i class="bi bi-car-front-fill me-2"></i>Total de Carros Cadastrados</h5>
                        <p class="card-text display-4" id="totalCarros"><?= $count_veiculos ?></p>
                    </div>
                </div>
            </div>

            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title"><i class="bi bi-person-fill me-2"></i>Total de Clientes</h5>
                        <p class="card-text display-4" id="totalClientes"><?= $count_clientes ?></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="row mt-4">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Total de Carros Disponíveis</h5>
                        <p class="card-text display-4" id="carrosDisponiveis"><?= $count_veiculos_disponiveis ?></p>
                    </div>
                </div>
            </div>

            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Total de Carros Alugados</h5>
                        <p class="card-text display-4" id="carrosAlugados"><?= $count_locacoes ?></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
            
        </div>
    </div>


@endsection