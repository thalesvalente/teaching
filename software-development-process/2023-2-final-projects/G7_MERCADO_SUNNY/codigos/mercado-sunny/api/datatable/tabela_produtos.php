<?php 
if ($resultado->num_rows > 0) {
    while($row = $resultado->fetch_assoc()) {
        echo "<tr>
            <td>".$row["id"]."</td>
            <td>".$row["nome"]."</td>
            <td>".$row["categoria"]."</td>
            <td>".$row["quantidade"]."</td>
            <td>".$row["preco"]."</td>
            <td>".$row["marca"]."</td>
            <td>".$row["peso_kg_l"]."</td>
            <td>
            <a href='#editarProdutoModal" . $row["id"] . "' class='btn btn-primary btn-circle btn-sm' data-toggle='modal'><i class='fas fa-pencil-alt'></i></a>
            <a href='#' class='btn btn-danger btn-circle btn-sm' data-toggle='modal' data-target='#removerProdutoModal" . $row["id"] . "'><i class='fas fa-trash'></i></a>
        </td>
        </tr>";


        // Modal de Edição para cada produto
        echo "
        <!-- Modal de Editar Produto -->
        <div class='modal fade' id='editarProdutoModal".$row["id"]."' tabindex='-1' role='dialog' aria-labelledby='exampleModalLabel' aria-hidden='true'>
            <div class='modal-dialog' role='document'>
                <div class='modal-content'>
                    <div class='modal-header'>
                        <h5 class='modal-title' id='exampleModalLabel'>Editar Produto</h5>
                        <button class='close' type='button' data-dismiss='modal' aria-label='Close'>
                            <span aria-hidden='true'>&times;</span>
                        </button>
                    </div>
                    <div class='modal-body'>
                        <!-- Formulário de Edição de Produto -->
                        <form action='#' method='post'>
                            <input type='hidden' name='produtoId' value='".$row["id"]."'>
                            <div class='form-group'>
                                <label for='nomeEdit'>Nome:</label>
                                <input type='text' class='form-control' id='nomeEdit' name='nomeEdit' value='".$row["nome"]."' required>
                            </div>
                            <div class='form-group'>
                                <label for='categoriaEdit'>Categoria:</label>
                                <select class='form-control' id='categoriaEdit' name='categoriaEdit' required>
                                    <option value='Alimentos Básicos' ".($row['categoria'] == 'Alimentos Básicos' ? 'selected' : '').">Alimentos Básicos</option>
                                    <option value='Hortifruti' ".($row['categoria'] == 'Hortifruti' ? 'selected' : '').">Hortifruti</option>
                                    <option value='Padaria' ".($row['categoria'] == 'Padaria' ? 'selected' : '').">Padaria</option>
                                    <option value='Bebidas' ".($row['categoria'] == 'Bebidas' ? 'selected' : '').">Bebidas</option>
                                    <option value='Congelados' ".($row['categoria'] == 'Congelados' ? 'selected' : '').">Congelados</option>
                                    <option value='Produtos de Limpeza' ".($row['categoria'] == 'Produtos de Limpeza' ? 'selected' : '').">Produtos de Limpeza</option>
                                    <option value='Higiene Pessoal' ".($row['categoria'] == 'Higiene Pessoal' ? 'selected' : '').">Higiene Pessoal</option>
                                    <option value='Produtos de Petshop' ".($row['categoria'] == 'Produtos de Petshop' ? 'selected' : '').">Produtos de Petshop</option>
                                    <option value='Farmácia' ".($row['categoria'] == 'Farmácia' ? 'selected' : '').">Farmácia</option>
                                </select>
                            </div>
                            <div class='form-group'>
                                <label for='quantidadeEdit'>Quantidade:</label>
                                <input type='text' class='form-control' id='quantidadeEdit' name='quantidadeEdit' value='".$row["quantidade"]."' required>
                            </div>
                            <div class='form-group'>
                                <label for='precoEdit'>Preço:</label>
                                <input type='text' class='form-control' id='precoEdit' name='precoEdit' value='".$row["preco"]."' required>
                            </div>
                            <div class='form-group'>
                                <label for='marcaEdit'>Marca:</label>
                                <input type='text' class='form-control' id='marcaEdit' name='marcaEdit' value='".$row["marca"]."' required>
                            </div>
                            <div class='form-group'>
                                <label for='pesoEdit'>Peso (Kg/L):</label>
                                <input type='text' class='form-control' id='pesoEdit' name='pesoEdit' value='".$row["peso_kg_l"]."' required>
                            </div>
                            <button type='submit' class='btn btn-primary' name='editarProduto'>Salvar Alterações</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>";

        // Modal de Remoção para cada produto
        echo "
        <!-- Modal de Remover Produto -->
        <div class='modal fade' id='removerProdutoModal".$row["id"]."' tabindex='-1' role='dialog' aria-labelledby='removerProdutoModalLabel' aria-hidden='true'>
            <div class='modal-dialog' role='document'>
                <div class='modal-content'>
                    <div class='modal-header'>
                        <h5 class='modal-title' id='removerProdutoModalLabel'>Remover Produto</h5>
                        <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                            <span aria-hidden='true'>&times;</span>
                        </button>
                    </div>
                    <div class='modal-body'>
                        <p>Deseja remover o produto?</p>
                    </div>
                    <div class='modal-footer'>
                        <button type='button' class='btn btn-secondary' data-dismiss='modal'>Não</button>
                        <a href='stock.php?removeProduto=".$row["id"]."' class='btn btn-primary'>Sim</a>
                    </div>
                </div>
            </div>
        </div>";
    }
} else {
    echo "0 results";
}
$mysqli->close();
?>