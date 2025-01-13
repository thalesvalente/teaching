package router

import (
	"construtora-API/internal/controllers" // Importa o pacote de controladores

	"github.com/gin-gonic/gin" // Importa o framework Gin para roteamento HTTP
)

// initializeRoutes configura as rotas do servidor HTTP
func initializeRoutes(r *gin.Engine) {
	
	// Rota para login
	r.POST("/Login", controllers.Login)

	// Grupo de rotas para funcionários
	funcionario := r.Group("/funcionario")
	{
		// Rota para cadastrar um novo funcionário
		funcionario.POST("/cadastro", controllers.CadastrarFuncionario)
		// Rota para buscar todos os funcionários
		funcionario.GET("/todos", controllers.BuscarTodosFuncionarios)
		// Rota para atualizar informações de um funcionário pelo ID
		funcionario.POST("/atualizar/:id", controllers.AtualizarFuncionario)
	}

	// Grupo de rotas para condomínios
	condominio := r.Group("/condominio")
	{
		// Rota para cadastrar um novo condomínio
		condominio.POST("/cadastrar", controllers.CadastrarCondominio)
		// Rota para listar todos os condomínios
		condominio.GET("/listar", controllers.ListarTodosCondominios)
	}

	// Grupo de rotas para clientes
	cliente := r.Group("/cliente")
	{
		// Rota para cadastrar um novo cliente
		cliente.POST("/cadastrar", controllers.CadastrarCliente)
		// Rota para listar todos os clientes
		cliente.GET("/listar", controllers.ListarTodosClientes)
	}

	// Grupo de rotas para imóveis
	imovel := r.Group("/imovel")
	{
		// Rota para cadastrar um novo imóvel
		imovel.POST("/cadastrar", controllers.CadastrarImovel)
		// Rota para listar todos os imóveis
		imovel.GET("/listar", controllers.ListarTodosImoveis)
		// Rota para buscar um imóvel por ID
		imovel.GET("/buscar/:id", controllers.BuscarImovelPorID)
	}
}
