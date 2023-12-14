<?php

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["editarProduto"])) {
    // Obtenha os dados do formulário de edição
    $produtoId = $_POST["produtoId"];
    $nomeEdit = $_POST["nomeEdit"];
    $categoriaEdit = $_POST["categoriaEdit"];
    $quantidadeEdit = $_POST["quantidadeEdit"];
    $precoEdit = $_POST["precoEdit"];
    $marcaEdit = $_POST["marcaEdit"];
    $pesoEdit = $_POST["pesoEdit"];

    // Obtenha os dados atuais do produto
    $consultaAtual = $mysqli->prepare("SELECT nome, categoria, quantidade, preco, marca, peso_kg_l FROM produtos WHERE id=?");
    $consultaAtual->bind_param("i", $produtoId);
    $consultaAtual->execute();
    $consultaAtual->bind_result($nomeAtual, $categoriaAtual, $quantidadeAtual, $precoAtual, $marcaAtual, $pesoAtual);
    $consultaAtual->fetch();
    $consultaAtual->close();

    // Verifique se os dados são os mesmos
    if (
        $nomeEdit == $nomeAtual &&
        $categoriaEdit == $categoriaAtual &&
        $quantidadeEdit == $quantidadeAtual &&
        $precoEdit == $precoAtual &&
        $marcaEdit == $marcaAtual &&
        $pesoEdit == $pesoAtual
    ) {
        // Os dados são os mesmos, exiba uma mensagem de erro
        $mensagemErroEditar = "Os dados são os mesmos. Nenhuma alteração foi feita.";

        // Redirecione de volta para a página principal com a mensagem de erro na URL
        header("Location: stock.php?mensagemErro=" . urlencode($mensagemErroEditar));
        exit();
    }

    // Verifique se o produto com os mesmos dados já existe
    $verificacao = $mysqli->prepare("SELECT id FROM produtos WHERE nome=? AND categoria=? AND preco=? AND marca=? AND peso_kg_l=? AND id<>?");
    $verificacao->bind_param("ssissi", $nomeEdit, $categoriaEdit, $precoEdit, $marcaEdit, $pesoEdit, $produtoId);
    $verificacao->execute();
    $verificacao->store_result();

    if ($verificacao->num_rows > 0) {
        // O produto com os mesmos dados já existe
        $mensagemErroEditar = "Produto já existente. Nenhuma alteração foi feita.";
        
        // Redirecione de volta para a página principal com a mensagem de erro na URL
        header("Location: stock.php?mensagemErro=" . urlencode($mensagemErroEditar));
        exit();
    } else {
        // Atualize os dados no banco de dados
        $atualizacao = $mysqli->prepare("UPDATE produtos SET nome=?, categoria=?, quantidade=?, preco=?, marca=?, peso_kg_l=? WHERE id=?");
        $atualizacao->bind_param("ssisssi", $nomeEdit, $categoriaEdit, $quantidadeEdit, $precoEdit, $marcaEdit, $pesoEdit, $produtoId);
        $atualizacao->execute();
        $atualizacao->close();

        // Redirecione de volta para a página principal com uma mensagem de sucesso na URL
        header("Location: stock.php?mensagemSucesso=Produto atualizado com sucesso!");
        exit();
    }
}
?>
