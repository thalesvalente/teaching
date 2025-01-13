package controllers

import (
	"construtora-API/internal/database"
	"construtora-API/internal/models"
	"construtora-API/internal/repository"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

// CadastrarImovel recebe os dados de um imóvel e os salva no banco de dados.
func CadastrarImovel(c *gin.Context) {
	// Declaração de uma variável para armazenar a requisição de imóvel recebida.
	var request models.Imovel

	// Faz o binding dos dados JSON da requisição para a struct Imovel.
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

	// Inicializa um novo repositório de imóvel, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioImovel(db)

	// Chama a função do repositório para cadastrar o imóvel no banco de dados.
	imovel, err := rep.CadastrarImovel(request)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna o imóvel cadastrado como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"imovel": imovel})
}

// ListarTodosImoveis recupera todos os imóveis cadastrados no banco de dados.
func ListarTodosImoveis(c *gin.Context) {
	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de imóvel, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioImovel(db)

	// Chama a função do repositório para listar todos os imóveis cadastrados.
	imoveis, err := rep.ListarTodosImoveis()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna a lista de imóveis como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"imoveis": imoveis})
}

// BuscarImovelPorID recupera um imóvel do banco de dados com base no ID fornecido na URL.
func BuscarImovelPorID(c *gin.Context) {
	// Obtém o ID do imóvel a ser buscado a partir dos parâmetros da URL.
	id := c.Param("id")
	if id == "" || id == " " {
		c.JSON(http.StatusBadRequest, gin.H{"message": "Identificador de coleção inválido"})
		return
	}

	// Converte o ID de string para uint64.
	imovelId, err := strconv.ParseUint(id, 10, 64)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Inicia uma conexão com o banco de dados.
	db, err := database.ConnectDB()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	defer db.Close() // Fecha a conexão com o banco de dados no final da função.

	// Inicializa um novo repositório de imóvel, passando a conexão do banco de dados.
	rep := repository.NovoRepositorioImovel(db)

	// Chama a função do repositório para buscar o imóvel pelo ID no banco de dados.
	imovel, err := rep.BuscarPorId(imovelId)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	// Retorna o imóvel encontrado como resposta da requisição.
	c.JSON(http.StatusOK, gin.H{"imovel": imovel})
}
