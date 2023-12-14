<?php

// Lógica para Adicionar Produto
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["addProduto"])) {
    // Obtenha os dados do formulário
    $nome = $_POST["nome"];
    $categoria = $_POST["categoria"];
    $quantidade = $_POST["quantidade"];
    $preco = $_POST["preco"];
    $marca = $_POST["marca"];
    $peso = $_POST["peso_kg_l"];

    // Verifique se o produto com os mesmos dados já existe
    $verificacao = $mysqli->prepare("SELECT id FROM produtos WHERE nome=? AND categoria=? AND preco=? AND marca=? AND peso_kg_l=?");
    $verificacao->bind_param("ssiss", $nome, $categoria, $preco, $marca, $peso);
    $verificacao->execute();
    $verificacao->store_result();

    if ($verificacao->num_rows > 0) {
        // O produto com os mesmos dados já existe
        $mensagemErroAdicionar = "Este produto já foi adicionado. Escolha um produto diferente.";
        
        // Redirecione de volta para a página principal com a mensagem de erro na URL
        header("Location: stock.php?mensagemErro=" . urlencode($mensagemErroAdicionar));
        exit();
    }

    // Execute a inserção no banco de dados
    $insercao = $mysqli->prepare("INSERT INTO produtos (nome, categoria, quantidade, preco, marca, peso_kg_l) VALUES (?, ?, ?, ?, ?, ?)");
    $insercao->bind_param("ssisss", $nome, $categoria, $quantidade, $preco, $marca, $peso);
    
    // Execute a inserção
    $insercao->execute();

    // Feche a instrução
    $insercao->close();

    // Redirecione de volta para a página principal com uma mensagem de sucesso na URL
    header("Location: stock.php?mensagemSucesso=Produto adicionado com sucesso!");
    exit();
}
?>
