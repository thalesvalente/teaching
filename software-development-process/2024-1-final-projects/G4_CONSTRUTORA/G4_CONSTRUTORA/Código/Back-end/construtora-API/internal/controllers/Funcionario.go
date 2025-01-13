package controllers

import (
	"construtora-API/internal/database"
	"construtora-API/internal/models"
	"construtora-API/internal/repository"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

// CadastrarFuncionario recebe os dados de um funcionário e os salva no banco de dados.
func CadastrarFuncionario(c *gin.Context) {
	// Declaração de uma variável para armazenar a requisição de funcionário recebida.
	var request models.Funcionario

	// Faz o binding dos dados JSON da requisição para a struct Funcionario.
	if err := c.ShouldBindJSON(&request); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}

	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de funcionário, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioFuncionario(db)

	// Chama a função do repositório para cadastrar o funcionário no banco de dados.
	funcionario, err := rep.CadastrarFuncionario(request)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna o funcionário cadastrado como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"Funcionario": funcionario})
}

// BuscarTodosFuncionarios recupera todos os funcionários cadastrados no banco de dados.
func BuscarTodosFuncionarios(c *gin.Context) {

	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de funcionário, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioFuncionario(db)

	// Chama a função do repositório para listar todos os funcionários cadastrados.
	funcionarios, err := rep.ListarTodosFuncionarios()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna a lista de funcionários como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"Funcionarios": funcionarios})
}

// AtualizarFuncionario atualiza os dados de um funcionário no banco de dados com base no ID fornecido.
func AtualizarFuncionario(c *gin.Context) {
	var request models.Funcionario

	// Faz o binding dos dados JSON da requisição para a struct Funcionario.
	if err := c.ShouldBindJSON(&request); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}

	// Obtém o ID do funcionário a ser atualizado a partir dos parâmetros da URL.
	funcionarioID := c.Param("id")
	if funcionarioID == "" || funcionarioID == " " {
		c.JSON(http.StatusBadRequest, gin.H{"message": "Identificador de Funcionário inválido"})
		return
	}

	// Converte o ID de string para uint64.
	id, err := strconv.ParseUint(funcionarioID, 10, 64)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	request.ID = id

	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de funcionário, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioFuncionario(db)

	// Chama a função do repositório para atualizar os dados do funcionário no banco de dados.
	err = rep.AtualizarFuncionario(request)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna uma mensagem de sucesso após atualizar os dados do funcionário.
	c.JSON(http.StatusOK, gin.H{"mensagem": "Dados atualizados com sucesso"})
}
