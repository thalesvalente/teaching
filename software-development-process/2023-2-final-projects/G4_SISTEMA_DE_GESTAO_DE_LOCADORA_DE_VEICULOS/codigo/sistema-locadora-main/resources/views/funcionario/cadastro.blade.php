@extends('dashboard_main')

@section('content')

    <div class="info-section bg-body-tertiary d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center">
        <h2 class="mb-0"><i class="bi bi-person-fill me-2"></i>Funcionário - Novo Cadastro</h2>
        <div class="d-flex gap-2">
            <a href="{{ route('funcionario.view-menu') }}" class="btn btn-danger" id="btnVoltar"><i class="bi bi-arrow-left-circle-fill"></i>Voltar</a>
        </div>
    </div>
    <div class="painel-acoes bg-body-tertiary p-3 info-section">
        <form action="{{ route('funcionario.cadastrar') }}" method="POST" enctype="multipart/form-data">
            @csrf
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="nome" class="form-label col-md-2">Nome</label>
                    <input type="text" class="form-control" id="nome" name="nome" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="cargo" class="form-label col-md-2">Cargo</label>
                    <select class="form-select" id="cargo" name="id_cargo" required>
                        <option >Selecione o cargo</option>
                        <option value="1">Gerente</option>
                        <option value="2">Atendente</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="cargo" class="form-label col-md-2">Unidade</label>
                    <select class="form-select" id="cargo" name="id_unidade_locadora" required>
                        <option value="">Selecione a unidade</option>
                        @foreach ($unidadesLocadora as $unidadeLocadora)
                            <option value={{ $unidadeLocadora->id_unidade_locadora }}> {{ $unidadeLocadora->cidade . ' - ' . $unidadeLocadora->id_unidade_locadora  }}</option>
                        @endforeach
                    </select>
                </div>
            </div>
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Cadastrar</button>
            </div>
        </form>
    </div>

@endsection