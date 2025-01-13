package controllers

import (
	"construtora-API/internal/database"
	"construtora-API/internal/models"
	"construtora-API/internal/repository"
	"net/http"

	"github.com/gin-gonic/gin"
)

// LoginInput define a estrutura esperada para os dados de entrada no endpoint de login.
type LoginInput struct {
	Cpf      string `json:"cpf"`      // CPF do usuário para autenticação
	Password string `json:"password"` // Senha do usuário para autenticação
}

// Login é um handler para o endpoint de login na API.
func Login(c *gin.Context) {
	// Variável para armazenar a requisição de login recebida.
	var request LoginInput

	// Faz o binding dos dados JSON da requisição para a struct LoginInput.
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
	repFuncionario := repository.NovoRepositorioFuncionario(db)

	// Busca no banco de dados um funcionário pelo CPF fornecido na requisição.
	retornoFuncionario, err := repFuncionario.BuscarPorCPF(request.Cpf)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}

	// Verifica se o retorno da busca por CPF é vazio (nenhum funcionário encontrado).
	if models.Funcionario{} == retornoFuncionario {
		// Se não encontrou um funcionário, tenta buscar um cliente com o mesmo CPF.
		repCliente := repository.NovoRepositorioCliente(db)
		cliente, err := repCliente.BuscarPorCPF(request.Cpf)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
			return
		}

		// Verifica se a senha fornecida na requisição corresponde à senha do cliente encontrado.
		if request.Password == cliente.Senha {
			c.JSON(http.StatusOK, gin.H{"sucesso": cliente})
			return
		}

		// Se a senha não corresponder, retorna uma mensagem de erro.
		c.JSON(http.StatusInternalServerError, gin.H{"message": "Credenciais Inválidas"})
	}

	// Se encontrou um funcionário pelo CPF, verifica se a senha fornecida corresponde à senha do funcionário.
	if request.Password == retornoFuncionario.Password {
		c.JSON(http.StatusOK, gin.H{"sucesso": retornoFuncionario})
		return
	}

	// Se nenhuma das verificações anteriores passou, retorna uma mensagem de erro de credenciais inválidas.
	c.JSON(http.StatusInternalServerError, gin.H{"message": "Credenciais Inválidas"})
}
