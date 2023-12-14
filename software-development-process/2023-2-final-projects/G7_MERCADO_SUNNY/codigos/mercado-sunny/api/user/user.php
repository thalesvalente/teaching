<?php
include '../security/protect.php';

if ($_SESSION['tipoUsuario'] == 'A') {
    header("Location: ../../pages/user_admin.php");
} else if ($_SESSION['tipoUsuario'] == 'F') {
    header("Location: ../../pages/user_funcionario.php");
} else {
    header("Location: ../../pages/404.php");
}
?>
