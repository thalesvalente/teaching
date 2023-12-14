<?php
    $mensagemErroEditar = '';

    // Lógica para Editar Usuário
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["editarUsuario"])) {
        // Obtenha os dados do formulário de edição
        $usuarioId = $_POST["usuarioId"];
        $numRegistroEdit = $_POST["numRegistroEdit"];
        $nomeEdit = $_POST["nomeEdit"];
        $senhaEdit = $_POST["senhaEdit"];
        $tipoUsuarioEdit = $_POST["tipoUsuarioEdit"];
    
        // Consulta SQL para verificar se o número de registro já existe
        $verificacao = $mysqli->prepare("SELECT id FROM usuarios WHERE numRegistro = ? AND id <> ?");
        $verificacao->bind_param("ii", $numRegistroEdit, $usuarioId);
        $verificacao->execute();
        $verificacao->store_result();
    
        if ($verificacao->num_rows > 0) {
            $mensagemErroEditar = "O número de registro já existe para outro usuário. Escolha outro.";
            header("Location: user_admin.php?mensagemErro=" . urlencode($mensagemErroEditar));
            exit();
        } else {
            // Consulta SQL para obter a senha atual
            $consultaSenha = "SELECT senha FROM usuarios WHERE id = ?";
            $stmtSenha = $mysqli->prepare($consultaSenha);
            $stmtSenha->bind_param("i", $usuarioId);
            $stmtSenha->execute();
            $stmtSenha->bind_result($senhaAtual);
            $stmtSenha->fetch();
            $stmtSenha->close();
    
            // Verifique se a senha foi alterada
            if (password_verify($senhaEdit, $senhaAtual)) {
                // Se a senha é a mesma, você pode lidar com isso aqui, como exibir uma mensagem de erro.
                $mensagemErroEditar = "A senha é a mesma. Nenhuma alteração foi feita.";
                
                // Redirecione de volta para a página principal com a mensagem de erro na URL
                header("Location: user_admin.php?mensagemErro=" . urlencode($mensagemErroEditar));
                exit();
            } else {
                // Hash da nova senha
                $senhaHash = password_hash($senhaEdit, PASSWORD_DEFAULT);
    
                // Atualize os dados no banco de dados
                $atualizacao = $mysqli->prepare("UPDATE usuarios SET numRegistro=?, nome=?, senha=?, tipoUsuario=? WHERE id=?");
                $atualizacao->bind_param("isssi", $numRegistroEdit, $nomeEdit, $senhaHash, $tipoUsuarioEdit, $usuarioId);
                $atualizacao->execute();
                $atualizacao->close();
    
                // Redirecione de volta para a página principal
                header("Location: user_admin.php?mensagemSucesso=Usuário atualizado com sucesso!");
                exit();
            }
        }
    }