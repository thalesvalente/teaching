<?php include 'layouts/head.php';
    include '../sgc/connection.php';

    // Consulta SQL para obter os dados da tabela de produtos
    $consulta = "SELECT id, nome, categoria, quantidade, preco, marca, peso_kg_l FROM produtos";
    $resultado = $mysqli->query($consulta);

    $consulta_menor_quantidade = "SELECT nome FROM produtos ORDER BY quantidade ASC LIMIT 1";
    $resultado_menor_quantidade = $mysqli->query($consulta_menor_quantidade);

    if ($resultado_menor_quantidade->num_rows > 0) {
        $produto_menor_quantidade = $resultado_menor_quantidade->fetch_assoc();
        $produto_menor_quantidade["nome"];
    }

    $consulta_maior_quantidade = "SELECT nome, quantidade FROM produtos ORDER BY quantidade DESC LIMIT 1";
    $resultado_maior_quantidade = $mysqli->query($consulta_maior_quantidade);

    if ($resultado_maior_quantidade->num_rows > 0) {
        $produto_maior_quantidade = $resultado_maior_quantidade->fetch_assoc();
        $produto_maior_quantidade["nome"];
    }

    $consulta_produto_mais_caro = "SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 1";
    $resultado_produto_mais_caro = $mysqli->query($consulta_produto_mais_caro);

    if ($resultado_produto_mais_caro->num_rows > 0) {
        $produto_mais_caro = $resultado_produto_mais_caro->fetch_assoc();
        $produto_mais_caro["nome"];
    }

    $consulta_categoria_mais_produtos = "SELECT categoria, COUNT(*) as total_produtos FROM produtos GROUP BY categoria ORDER BY total_produtos DESC LIMIT 1";
    $resultado_categoria_mais_produtos = $mysqli->query($consulta_categoria_mais_produtos);
    
    if ($resultado_categoria_mais_produtos->num_rows > 0) {
        $categoria_mais_produtos = $resultado_categoria_mais_produtos->fetch_assoc();
        $categoria_mais_produtos["categoria"];
    }


?>

<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>


<body id="page-top">
    <?php include 'layouts/sidebar.php'; ?>
        <?php include 'layouts/topbar.php'; ?>
        
                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Content Row -->
                    <div class="row">

                        <!-- Card -->
                        <div class="col-xl-3 col-md-6 mb-4">
                            <div class="card border-left-primary shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                                Produto mais caro</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $produto_mais_caro["nome"]; ?></div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Card -->
                        <div class="col-xl-3 col-md-6 mb-4">
                            <div class="card border-left-success shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-success text-uppercase mb-1">
                                                Categoria com mais produtos</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $categoria_mais_produtos["categoria"]; ?></div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-boxes fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Card -->
                        <div class="col-xl-3 col-md-6 mb-4">
                            <div class="card border-left-info shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-info text-uppercase mb-1">Produto em maior quantidade
                                            </div>
                                            <div class="row no-gutters align-items-center">
                                                <div class="col-auto">
                                                    <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800"><?php echo $produto_maior_quantidade["nome"]; ?></div>
                                                </div>
                                                <div class="col">
                                                    <div class="progress progress-sm mr-2">
                                                        <div class="progress-bar bg-info" role="progressbar"
                                                            style="width: 50%" aria-valuenow="50" aria-valuemin="0"
                                                            aria-valuemax="100"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-chart-line fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pending Requests Card -->
                        <div class="col-xl-3 col-md-6 mb-4">
                            <div class="card border-left-warning shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">
                                                Produto em falta</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $produto_menor_quantidade["nome"]; ?></div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-caret-down fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Content Row -->

                    <div class="row">


                        <div class="col-xl-12 col-lg-7">
                            <div class="card shadow mb-4">
                                <!-- Card Header - Dropdown -->
                                <div
                                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                                    <h6 class="m-0 font-weight-bold text-primary">Categorias com mais estoque</h6>
                                    <div class="dropdown no-arrow">
                                        <div class="dropdown-menu dropdown-menu-right shadow animated--fade-in"
                                            aria-labelledby="dropdownMenuLink">
                                            
                                        </div>
                                    </div>
                                </div>
                                <!-- Card Body -->
                                <div class="card-body">
                                    <div class="chart-area-categoria">
                                        <div id="chartCategoria" ></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


            </div>
            <!-- End of Main Content -->

            <?php include 'layouts/footer.php'; ?>

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>


    <!-- Bootstrap core JavaScript-->
    <script src="../vendor/jquery/jquery.min.js"></script>
    <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="../vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="../js/sb-admin-2.min.js"></script>

    <!-- Page level plugins -->
    <script src="../vendor/chart.js/Chart.min.js"></script>

    <!-- Page level custom scripts -->
    <script src="../js/demo/chart-area-demo.js"></script>


</body>

</html>