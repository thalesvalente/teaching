$(document).ready(function () {
    // Adicionar evento de clique ao botão de remover
    $('a[data-toggle="modal"]').click(function () {
        var target = $(this).data('target');
        $('#confirmarRemocao').attr('href', target);
        $('#removerProdutoModal').modal('show');
    });
});

// Função para obter parâmetros da URL
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

// Verifique se há uma mensagem de erro na URL e exiba um alerta
var mensagemErro = getParameterByName('mensagemErro');
if (mensagemErro) {
    alert(mensagemErro);
}

// Verifique se há uma mensagem de sucesso na URL e exiba um alerta
var mensagemSucesso = getParameterByName('mensagemSucesso');
if (mensagemSucesso) {
    alert(mensagemSucesso);
}

// Verifique se o parâmetro 'removido' está presente na URL
var removido = getParameterByName('removido');

// Se 'removido' estiver presente, exiba uma mensagem de sucesso
if (removido === 'true') {
    // Adicione aqui o código para exibir a mensagem de remoção com sucesso
    alert('Produto removido com sucesso!');
}