<?php

$mensagemErro = '';

// Lógica para Adicionar Usuário
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["addUsuario"])) {
    // Obtenha os dados do formulário
    $numRegistro = $_POST["numRegistro"];
    $nome = $_POST["nome"];
    $senha = password_hash($_POST["senha"], PASSWORD_DEFAULT); // Criptografa a senha
    $tipoUsuario = $_POST["tipoUsuario"];

    // Verifique se o número de registro já existe
    $verificacao = $mysqli->prepare("SELECT id FROM usuarios WHERE numRegistro = ?");
    $verificacao->bind_param("i", $numRegistro);
    $verificacao->execute();
    $verificacao->store_result();

    if ($verificacao->num_rows > 0) {
        $mensagemErroAdicionar = "O número de registro já existe. Escolha outro número.";
        header("Location: user_admin.php?mensagemErro=" . urlencode($mensagemErroAdicionar));
        exit();
    } else {
        // Execute a inserção no banco de dados usando declaração preparada
        $insercao = $mysqli->prepare("INSERT INTO usuarios (numRegistro, nome, senha, tipoUsuario) VALUES (?, ?, ?, ?)");
        $insercao->bind_param("isss", $numRegistro, $nome, $senha, $tipoUsuario);

        // Execute a inserção
        $insercao->execute();

        // Feche a instrução
        $insercao->close();

        // Redirecione de volta para a página principal
        header("Location: user_admin.php");
        exit();
    }
}