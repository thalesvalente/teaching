<?php 

    ob_start(); // Inicia o buffer de saída
    include 'layouts/head.php';
    include 'layouts/sidebar.php';
    include 'layouts/topbar.php';
    include '../sgc/connection.php';

    $aa = '';

    // Consulta SQL para obter os dados da tabela de usuários
    $consulta = "SELECT id, numRegistro, nome, senha, tipoUsuario FROM usuarios";
    $resultado = $mysqli->query($consulta);
    
    include '../api/add/adicionar_usuario.php';
    include '../api/edit/editar_admin.php';
    include '../api/remove/remover_admin.php';


?>

<body id="page-top">
    <!-- Begin Page Content -->
    <div class="container-fluid">
        <!-- Page Heading -->
        <div class="d-sm-flex align-items-center justify-content-between mb-4">
                        <h1 class="h3 mb-0 text-gray-800">Usuário</h1>
                        <a href="#" data-toggle="modal" data-target="#logoutModal" class="btn btn-primary btn-icon-split">
                                <span class="icon text-white-50">
                                    <i class="fas fa-sign-out-alt"></i>
                                </span>
                                <span class="text">Logout</span>

                        </a>
                    </div>
                    

        <div class="card shadow mb-4">
        <div class="card-header py-3 d-flex justify-content-between align-items-center">
            <div>
                <h6 class="m-0 font-weight-bold text-primary">Configurações de Usuário</h6>
            </div>
            <div class="mb-4">
                <form action="#" method="post">
                    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#adicionarUsuarioModal">Adicionar Usuário</button>
                    </form>
            </div>
        </div>

        

            
            <div class="card-body">
                <div class="table-responsive">
		            <!-- Modal de Adicionar Usuário -->
                    <div class="modal fade" id="adicionarUsuarioModal" tabindex="-1" role="dialog" aria-labelledby="adicionarUsuarioModalLabel" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="adicionarUsuarioModalLabel">Adicionar Usuário</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <!-- Formulário de Adição de Usuário -->
                                    <form action="#" method="post">
                                        <div class="form-group">
                                            <label for="numRegistro">Registro:</label>
                                            <input type="number" class="form-control" id="numRegistro" name="numRegistro" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="nome">Nome:</label>
                                            <input type="text" class="form-control" id="nome" name="nome" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="senha">Senha:</label>
                                            <input type="password" class="form-control" id="senha" name="senha" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="tipoUsuario">Permissão:</label>
                                            <select class="form-control" id="tipoUsuario" name="tipoUsuario" required>
                                                <option value="A">Administrador</option>
                                                <option value="F">Funcionário</option>
                                            </select>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                            <button type="submit" name="addUsuario" class="btn btn-primary">Adicionar</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>

                    <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                        <thead>
                            <tr>
                                <th>Registro</th>
                                <th>Nome</th>
                                <th>Permissões</th>
                                <th>Ações</th> 
                            </tr>
                        </thead>
                        <tbody>
                            <?php include '../api/datatable/tabela_admin.php'?>
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

    <script src="../js/user_admin.js"></script>
    
    <!-- Script para alternar a visibilidade da senha -->
    <script src="../js/toggle_password.js"></script>


</body>

</html>