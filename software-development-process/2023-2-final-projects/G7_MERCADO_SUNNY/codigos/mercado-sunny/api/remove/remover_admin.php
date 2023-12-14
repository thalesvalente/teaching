<?php
// Lógica para Remover Usuário
if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["removeUsuario"])) {
    $id = $_GET["removeUsuario"];

    // Execute a remoção no banco de dados
    $remocao = $mysqli->prepare("DELETE FROM usuarios WHERE id = ?");
    $remocao->bind_param("i", $id);
    $remocao->execute();

    // Feche a instrução
    $remocao->close();

    // Redirecione de volta para a página principal com uma mensagem de sucesso na URL
    header("Location: user_admin.php?removido=true");
    ob_end_flush(); // Descarrega o buffer de saída e envia para o navegador
    exit(); // Certifique-se de sair após o redirecionamento
}
?>
