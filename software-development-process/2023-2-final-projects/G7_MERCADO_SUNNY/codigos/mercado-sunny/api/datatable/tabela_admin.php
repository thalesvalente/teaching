<?php 
    if ($resultado->num_rows > 0) {
        while ($row = $resultado->fetch_assoc()) {
            echo "<tr>
                <td>" . $row["numRegistro"] . "</td>
                <td>" . $row["nome"] . "</td>
                <td>" . ($row["tipoUsuario"] == 'A' ? 'Administrador' : 'Funcionário') . "</td>
                <td>
                    <a href='#editarUsuarioModal" . $row["id"] . "' class='btn btn-primary btn-circle btn-sm' data-toggle='modal'><i class='fas fa-pencil-alt'></i></a>
                    <a href='#' class='btn btn-danger btn-circle btn-sm' data-toggle='modal' data-target='#removerUsuarioModal" . $row["id"] . "'><i class='fas fa-trash'></i></a>
                </td>
            </tr>";


        // Modal de Edição para cada usuário
        echo "
        <!-- Modal de Editar Usuário -->
        <div class='modal fade' id='editarUsuarioModal".$row["id"]."' tabindex='-1' role='dialog' aria-labelledby='exampleModalLabel' aria-hidden='true'>
            <div class='modal-dialog' role='document'>
                <div class='modal-content'>
                    <div class='modal-header'>
                        <h5 class='modal-title' id='exampleModalLabel'>Editar Usuário</h5>
                        <button class='close' type='button' data-dismiss='modal' aria-label='Close'>
                            <span aria-hidden='true'>&times;</span>
                        </button>
                    </div>
                    <div class='modal-body'>
                        <!-- Formulário de Edição de Usuário -->
                        <form action='#' method='post'>
                            <input type='hidden' name='usuarioId' value='".$row["id"]."'>
                            <div class='form-group'>
                                <label for='numRegistroEdit'>Registro:</label>
                                <input type='number' class='form-control' id='numRegistroEdit' name='numRegistroEdit' value='".$row["numRegistro"]."' required>
                            </div>
                            <div class='form-group'>
                                <label for='nomeEdit'>Nome:</label>
                                <input type='text' class='form-control' id='nomeEdit' name='nomeEdit' value='".$row["nome"]."' required>
                            </div>
                            <div class='form-group'>   
                                <label for='senhaEdit'>Senha:</label>
                                <div class='form-group position-relative'>
                                    <input type='password' class='form-control form-control-user form-control-password' id='senhaEdit' name='senhaEdit' placeholder='Nova senha' required>
                                    <!-- <span data-toggle='#senhaEdit' class='fa fa-fw fa-eye field-icon toggle-password'></span> -->
                                </div>
                            </div>

                            <div class='form-group'>
                                <label for='tipoUsuarioEdit'>Pemissões:</label>
                                <select class='form-control' id='tipoUsuarioEdit' name='tipoUsuarioEdit' required>
                                    <option value='A' ".($row['tipoUsuario'] == 'A' ? 'selected' : '').">Administrador</option>
                                    <option value='F' ".($row['tipoUsuario'] == 'F' ? 'selected' : '').">Funcionário</option>
                                </select>
                            </div>
                            <button type='submit' class='btn btn-primary' name='editarUsuario'>Salvar Alterações</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>";

        // Modal de Remoção para cada usuário
        echo "
        <!-- Modal de Remover Usuário -->
        <div class='modal fade' id='removerUsuarioModal".$row["id"]."' tabindex='-1' role='dialog' aria-labelledby='removerUsuarioModalLabel' aria-hidden='true'>
            <div class='modal-dialog' role='document'>
                <div class='modal-content'>
                    <div class='modal-header'>
                        <h5 class='modal-title' id='removerUsuarioModalLabel'>Remover Usuário</h5>
                        <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                            <span aria-hidden='true'>&times;</span>
                        </button>
                    </div>
                    <div class='modal-body'>
                        <p>Deseja remover o usuário?</p>
                    </div>
                    <div class='modal-footer'>
                        <button type='button' class='btn btn-secondary' data-dismiss='modal'>Não</button>
                        <a href='user_admin.php?removeUsuario=".$row["id"]."' class='btn btn-primary'>Sim</a>
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

