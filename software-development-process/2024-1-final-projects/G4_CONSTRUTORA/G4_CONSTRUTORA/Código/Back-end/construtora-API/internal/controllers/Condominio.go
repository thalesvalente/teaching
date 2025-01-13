package controllers

import (
	"construtora-API/internal/database"
	"construtora-API/internal/models"
	"construtora-API/internal/repository"
	"net/http"

	"github.com/gin-gonic/gin"
)

// CadastrarCondominio é um handler para a rota de cadastro de condomínios.
func CadastrarCondominio(c *gin.Context) {
	var request models.CondominioInput

	// Faz o binding dos dados JSON da requisição para a struct CondominioInput.
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
	repEndereco := repository.NovoRepositorioEndereco(db)

	// Chama a função do repositório para cadastrar um novo endereço e retorna o ID do endereço.
	idEndereco, err := repEndereco.CadastrarEndereco(request.Rua, request.Numero, request.Cidade, request.Estado, request.Cep)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Inicializa um novo repositório de condomínio, passando a conexão do banco de dados.
	repCondominio := repository.NovoRepositorioCondominio(db)

	// Chama a função do repositório para cadastrar um novo condomínio.
	err = repCondominio.CadastrarCondominio(request.Nome, request.QuantidadeImoveis, request.Aminidades, request.Taxa, request.AnoConstrucao, request.Status, idEndereco)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna uma resposta de sucesso após cadastrar o condomínio.
	c.JSON(http.StatusOK, gin.H{"sucesso": "condomínio cadastrado com sucesso"})
}

// ListarTodosCondominios é um handler para a rota de listagem de todos os condomínios.
func ListarTodosCondominios(c *gin.Context) {
	
	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de condomínio, passando a conexão do banco de dados.
	repCondominio := repository.NovoRepositorioCondominio(db)

	// Chama a função do repositório para listar todos os condomínios cadastrados.
	condominios, err := repCondominio.ListarTodosCondominios()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna a lista de condomínios como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"condominios": condominios})
}
