<?php
if ($resultado->num_rows > 0) {
    while ($row = $resultado->fetch_assoc()) {
        echo "<tr>
            <td>" . $row["numRegistro"] . "</td>
            <td>" . $row["nome"] . "</td>
            <td>" . ($row["tipoUsuario"] == 'A' ? 'Administrador' : 'Funcionário') . "</td>
            <td>
                <a href='#editarUsuarioModal" . $row["id"] . "' class='btn btn-primary btn-circle btn-sm' data-toggle='modal'><i class='fas fa-pencil-alt'></i></a>
            </td>
        </tr>";
        

    // Modal de Edição para cada usuário
    echo "
    <!-- Modal de Editar Usuário -->
    <div class='modal fade' id='editarUsuarioModal".$_SESSION["id"]."' tabindex='-1' role='dialog' aria-labelledby='exampleModalLabel' aria-hidden='true'>
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
                        <input type='hidden' name='usuarioId' value='".$_SESSION["id"]."'>
                        <div class='form-group'>
                            <label for='nomeEdit'>Nome:</label>
                            <input type='text' class='form-control' id='nomeEdit' name='nomeEdit' placeholder='Nova senha' required>
                        </div>

                        <div class='form-group'>   
                            <label for='senhaEdit'>Senha:</label>
                            <div class='form-group position-relative'>
                                <input type='password' class='form-control form-control-user form-control-password' id='senhaEdit' name='senhaEdit' required>
                                <!-- <span toggle='#senha' class='fa fa-fw fa-eye field-icon toggle-password'></span> -->
                            </div>
                        </div>

                        <button type='submit' class='btn btn-primary' name='editarUsuario'>Salvar Alterações</button>
                    </form>
                </div>
            </div>
        </div>
    </div>";
}
} else {
echo "0 results";
}
$mysqli->close();