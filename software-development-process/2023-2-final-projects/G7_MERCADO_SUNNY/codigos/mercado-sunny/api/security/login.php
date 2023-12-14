<?php

$registroError = $senhaError = $loginError = '';

if (isset($_POST['loginButton'])) {
    $registro = trim($_POST['registro']);
    $senha = trim($_POST['senha']);

    if (empty($registro)) {
        $registroError = "Preencha seu registro.";
    } elseif (empty($senha)) {
        $senhaError = "Preencha sua senha.";
    } else {
        $registro = $mysqli->real_escape_string($registro);

        // Consulta SQL usando declaração preparada
        $consulta = $mysqli->prepare("SELECT id, nome, senha, tipoUsuario FROM usuarios WHERE numRegistro = ?");
        $consulta->bind_param("i", $registro);
        $consulta->execute();
        $resultado = $consulta->get_result();
        $consulta->close();

        if ($resultado->num_rows == 1) {
            $usuario = $resultado->fetch_assoc();

            // Verifica se a senha fornecida coincide com a senha criptografada no banco de dados
            
            if (password_verify($senha, $usuario['senha'])) {
                if (!isset($_SESSION)) {
                    session_start();
                }
            
                $_SESSION['id'] = $usuario['id'];
                $_SESSION['nome'] = $usuario['nome'];
                $_SESSION['senha'] = $usuario['senha'];
                $_SESSION['numRegistro'] = $usuario['nome'];
                $_SESSION['tipoUsuario'] = $usuario['tipoUsuario'];
            
            
                header("Location: pages/dashboard.php");
                exit();
            } else {
                $loginError = "Falha ao logar! Registro ou senha incorretos";
            }
            
        } else {
            $loginError = "Falha ao logar! Registro ou senha incorretos";
        }
    }
}
?>
