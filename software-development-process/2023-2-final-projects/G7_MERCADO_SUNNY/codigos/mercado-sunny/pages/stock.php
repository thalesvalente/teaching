<?php 
    ob_start(); // Inicia o buffer de saída
    include 'layouts/head.php'; 
    include 'layouts/sidebar.php'; 
    include 'layouts/topbar.php'; 
    include '../sgc/connection.php';

    // Consulta SQL para obter os dados da tabela de produtos
    $consulta = "SELECT id, nome, categoria, quantidade, preco, marca, peso_kg_l FROM produtos";
    $resultado = $mysqli->query($consulta);

    include '../api/add/adicionar_produto.php';
    include '../api/edit/editar_produto.php';
    include '../api/remove/remover_produto.php';

    


?>

<body id="page-top">
    <!-- Begin Page Content -->
    <div class="container-fluid">
        <!-- Page Heading -->
        <div class="d-sm-flex align-items-center justify-content-between mb-4">
            <h1 class="h3 mb-0 text-gray-800">Estoque</h1>
        </div>
        <!-- DataTales Example -->
        <div class="card shadow mb-4">
            <div class="card-header py-3 d-flex justify-content-between align-items-center">
                <div>
                    <h6 class="m-0 font-weight-bold text-primary">Gerenciamento</h6>
                </div>
                <div class="mb-4">
                    <form action="#" method="post">
                        <!-- Campos do formulário (nome, categoria, quantidade, etc.) -->
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#adicionarProdutoModal">Adicionar Produto</button>
                    </form>
                </div>
            </div>

            <div class="card-body">
                <div class="table-responsive">
                    <!-- Formulário de Adição de Produto -->
                    

		    <!-- Modal de Adicionar Produto -->
                    <div class="modal fade" id="adicionarProdutoModal" tabindex="-1" role="dialog" aria-labelledby="adicionarProdutoModalLabel" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="adicionarProdutoModalLabel">Adicionar Produto</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <!-- Formulário de Adição de Produto -->
                                    <form action="#" method="post">
                                        <div class="form-group">
                                            <label for="nome">Nome:</label>
                                            <input type="text" class="form-control" id="nome" name="nome" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="categoria">Categoria:</label>
                                            <select class="form-control" id="categoria" name="categoria" required>
                                                <option value="Alimentos Básicos">Alimentos Básicos</option>
                                                <option value="Hortifruti">Hortifruti</option>
                                                <option value="Padaria">Padaria</option>
                                                <option value="Bebidas">Bebidas</option>
                                                <option value="Congelados">Congelados</option>
                                                <option value="Produtos de Limpeza">Produtos de Limpeza</option>
                                                <option value="Higiene Pessoal">Higiene Pessoal</option>
                                                <option value="Produtos de Petshop">Produtos de Petshop</option>
                                                <option value="Farmácia">Farmácia</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="quantidade">Quantidade:</label>
                                            <input type="text" class="form-control" id="quantidade" name="quantidade" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="preco">Preço:</label>
                                            <input type="text" class="form-control" id="preco" name="preco" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="marca">Marca:</label>
                                            <input type="text" class="form-control" id="marca" name="marca" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="peso_kg_l">Peso (Kg/L):</label>
                                            <input type="text" class="form-control" id="peso_kg_l" name="peso_kg_l" required>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                            <button type="submit" name="addProduto" class="btn btn-primary">Adicionar</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>

                    <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nome</th>
                                <th>Categoria</th>
                                <th>Quantidade</th>
                                <th>Preço</th>
                                <th>Marca</th>
                                <th>Peso (Kg/L)</th>
                                <th>Ações</th> <!-- Coluna para botões de ação -->
                            </tr>
                        </thead>
                        <tfoot>
                            <tr>
                                <th>ID</th>
                                <th>Nome</th>
                                <th>Categoria</th>
                                <th>Quantidade</th>
                                <th>Preço</th>
                                <th>Marca</th>
                                <th>Peso (Kg/L)</th>
                                <th>Ações</th>
                            </tr>
                        </tfoot>
                        <tbody>
                            <?php include '../api/datatable/tabela_produtos.php';?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    <!-- /.container-fluid -->

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
    <script src="../vendor/datatables/jquery.dataTables.min.js"></script>
    <script src="../vendor/datatables/dataTables.bootstrap4.min.js"></script>

    <!-- Page level custom scripts -->
    <script src="../js/demo/datatables-demo.js"></script>
    <script src="../js/stock.js"></script>



</body>

</html>