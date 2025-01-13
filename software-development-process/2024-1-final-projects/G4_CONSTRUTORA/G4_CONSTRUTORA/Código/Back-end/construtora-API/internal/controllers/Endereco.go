package controllers

import (
	"construtora-API/internal/database"
	"construtora-API/internal/models"
	"construtora-API/internal/repository"
	"net/http"

	"github.com/gin-gonic/gin"
)

// CadastrarEndereco é um handler para a rota de cadastro de endereço.
func CadastrarEndereco(c *gin.Context) {

	// Declaração de uma variável para armazenar a requisição de endereço recebida.
	var request models.Endereco

	// Faz o binding dos dados JSON da requisição para a struct Endereco.
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

	// Inicializa um novo repositório de endereço, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioEndereco(db)

	// Chama a função do repositório para cadastrar o endereço no banco de dados e retorna o ID do endereço cadastrado.
	id, err := rep.CadastrarEndereco(request.Rua, request.Numero, request.Cidade, request.Estado, request.Cep)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna o ID do endereço cadastrado como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"id_endereco": id})
}
