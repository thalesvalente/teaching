<?php

$mensagemErroEditar = '';

// Lógica para Editar Usuário
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["editarUsuario"])) {
    // Obtenha os dados do formulário de edição
    $usuarioId = $_POST["usuarioId"];
    $nomeEdit = $_POST["nomeEdit"];
    $senhaEdit = $_POST["senhaEdit"];

    // Consulta SQL para verificar se a senha já existe
    $verificacao = $mysqli->prepare("SELECT id FROM usuarios WHERE senha = ? AND id <> ?");
    $verificacao->bind_param("si", $senhaEdit, $usuarioId);
    $verificacao->execute();
    $verificacao->store_result();

    if ($verificacao->num_rows > 0) {
        $mensagemErroEditar = "A senha já existe para outro usuário. Escolha outra senha.";
        header("Location: user_funcionario.php?mensagemErro=" . urlencode($mensagemErroEditar));
        exit();
    } else {
        // Consulta SQL para obter a senha atual
        $consulta = "SELECT senha FROM usuarios WHERE id = ?";
        $stmt = $mysqli->prepare($consulta);
        $stmt->bind_param("i", $usuarioId);
        $stmt->execute();
        $stmt->bind_result($senhaAtual);
        $stmt->fetch();
        $stmt->close();

        // Verifique se a senha foi alterada
        if (password_verify($senhaEdit, $senhaAtual)) {
            // Se a senha é a mesma, você pode lidar com isso aqui, como exibir uma mensagem de erro.
            $mensagemErroEditar = "A senha é a mesma. Nenhuma alteração foi feita.";
            
            // Redirecione de volta para a página principal com a mensagem de erro na URL
            header("Location: user_funcionario.php?mensagemErro=" . urlencode($mensagemErroEditar));
            exit();
        } else {
            // Hash da nova senha
            $senhaHash = password_hash($senhaEdit, PASSWORD_DEFAULT);

            // Atualize os dados no banco de dados
            $atualizacao = $mysqli->prepare("UPDATE usuarios SET nome=?, senha=? WHERE id=?");
            $atualizacao->bind_param("ssi", $nomeEdit, $senhaHash, $usuarioId);
            $atualizacao->execute();
            $atualizacao->close();

            // Redirecione de volta para a página principal
            header("Location: user_funcionario.php?mensagemSucesso=Usuário atualizado com sucesso!");
            exit();
        }
    }
}