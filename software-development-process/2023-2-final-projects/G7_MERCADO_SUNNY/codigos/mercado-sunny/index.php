<?php
include 'sgc/connection.php';
include 'api/security/login.php';
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta author="José Victor Brito Costa" content="">

    <title>Mercadinho</title>

    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <link rel="icon" href="img/favicon.ico" type="image/x-icon">
    <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">

    <link href="css/sb-admin-2.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <style>

    </style>

</head>

<body class="bg-gradient-primary">

    <div class="container">

        <!-- Outer Row -->
        <div class="row justify-content-center">

            <div class="col-xl-10 col-lg-12 col-md-9">

                <div class="card o-hidden border-0 shadow-lg my-5">
                    <div class="card-body p-0">
                        <!-- Nested Row within Card Body -->
                        <div class="row">
                            <div class="col-lg-6 d-none d-lg-block">
                                <img src="img/login.jpeg" width="440" height="420">
                            </div>
                            <div class="col-lg-6">
                                <div class="p-5">
                                    <div class="text-center">
                                        <h1 class="h4 text-gray-900 mb-4">Sunny!</h1>
                                    </div>
                                    <form class="user" action="" method="POST">
                                    <div class="form-group">
                                            <input name="registro" type="number" class="form-control form-control-user"
                                                id="registro" aria-describedby="userHelp"
                                                placeholder="Número de Registro" required>
                                            <!-- Exibir mensagem de erro para o registro -->
                                            <div class="error-message"><?php echo $registroError; ?></div>
                                        </div>
                                        <div class="form-group position-relative">
                                            <input name="senha" type="password" class="form-control form-control-user form-control-password"
                                                id="senha" placeholder="Senha" required>
                                            <!-- Botão para alternar a visibilidade da senha -->
                                            <span toggle="#senha" class="fa fa-fw fa-eye field-icon toggle-password"></span>
                                            <!-- Exibir mensagem de erro para a senha -->
                                            <div class="error-message"><?php echo $senhaError; ?></div>
                                        </div>

                                        <button type="submit" name="loginButton"
                                            class="btn btn-primary btn-user btn-block">Login</button>
                                        <!-- Exibir mensagem de erro para o login -->
                                        <div class="error-message"><?php echo $loginError; ?></div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>

    <!-- Script para alternar a visibilidade da senha -->
    <script src="js/toggle_password.js"></script>

</body>

</html>


