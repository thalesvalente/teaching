package controllers

import (
	"construtora-API/internal/database"
	"construtora-API/internal/models"
	"construtora-API/internal/repository"
	"net/http"

	"github.com/gin-gonic/gin"
)

// CadastrarCliente é um handler para a rota de cadastro de clientes.
func CadastrarCliente(c *gin.Context) {
	var request models.Cliente

	// Faz o binding dos dados JSON da requisição para a struct Cliente.
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

	// Inicializa um novo repositório de cliente, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioCliente(db)

	// Chama a função do repositório para cadastrar o cliente no banco de dados.
	cliente, err := rep.CadastrarCliente(request)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna o cliente cadastrado como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"cliente": cliente})
}

// ListarTodosClientes é um handler para a rota de listagem de todos os clientes.
func ListarTodosClientes(c *gin.Context) {
	
	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de cliente, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioCliente(db)

	// Chama a função do repositório para listar todos os clientes cadastrados.
	clientes, err := rep.ListarTodosClientes()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna a lista de clientes como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"clientes": clientes})
}
