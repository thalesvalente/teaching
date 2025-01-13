package repository

import (
	"construtora-API/internal/models" // Importa o pacote onde os modelos de dados são definidos
	"database/sql"                    // Importa o pacote de SQL que fornece uma interface genérica para banco de dados
)

// Cliente é uma struct que contém uma referência ao banco de dados
type Cliente struct {
	db *sql.DB
}

// NovoRepositorioCliente cria um novo repositório de clientes com uma conexão ao banco de dados
func NovoRepositorioCliente(db *sql.DB) *Cliente {
	return &Cliente{db} // Retorna um ponteiro para Cliente com a conexão ao banco de dados
}

// CadastrarCliente insere um novo cliente no banco de dados
func (c *Cliente) CadastrarCliente(cliente models.Cliente) (models.Cliente, error) {
	sql := "INSERT INTO Clientes (cpf, nome, numero_de_filhos, estado_civil, renda, senha) VALUES ($1, $2, $3, $4, $5, $6)"

	// Prepara a instrução SQL para execução
	stmt, err := c.db.Prepare(sql)
	if err != nil {
		return models.Cliente{}, err // Retorna um cliente vazio e o erro se ocorrer um problema na preparação da instrução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	// Executa a instrução SQL com os dados do cliente
	_, err = stmt.Exec(cliente.Cpf, cliente.Nome, cliente.NumeroFilhos, cliente.EstadoCivil, cliente.Renda, cliente.Senha)
	if err != nil {
		return models.Cliente{}, err // Retorna um cliente vazio e o erro se ocorrer um problema na execução
	}
	
	return cliente, err // Retorna o cliente e nil indicando que não houve erros
}

// ListarTodosClientes retorna uma lista de todos os clientes do banco de dados
func (c *Cliente) ListarTodosClientes() ([]models.Cliente, error){
	sql := "SELECT * FROM Clientes"

	// Executa a instrução SQL para selecionar todos os clientes
	stmt, err := c.db.Query(sql)
	if err != nil {
		return nil, err // Retorna nil e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var clientes []models.Cliente

	// Itera sobre os resultados da consulta
	for stmt.Next() {
		var cliente models.Cliente
		// Escaneia os dados do cliente na variável cliente
		if err = stmt.Scan(
			&cliente.ID, 
			&cliente.Cpf, 
			&cliente.Nome,
			&cliente.NumeroFilhos, 
			&cliente.EstadoCivil,
			&cliente.Renda,
			&cliente.CreatedAt,
			&cliente.UpdatedAt,
			&cliente.Senha,
		); err != nil {
			return nil, err // Retorna nil e o erro se ocorrer um problema na leitura dos dados
		}

		clientes = append(clientes, cliente) // Adiciona o cliente na lista de clientes
	}

	return clientes, nil // Retorna a lista de clientes e nil indicando que não houve erros
}

// BuscarPorCPF busca um cliente no banco de dados pelo CPF
func (c *Cliente) BuscarPorCPF(cpf string) (models.Cliente, error) {
	query := "SELECT * FROM Clientes where cpf = $1"
	
	// Executa a instrução SQL para selecionar o cliente pelo CPF
	stmt, err := c.db.Query(query, cpf)
	if err != nil {
		return models.Cliente{}, err // Retorna um cliente vazio e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var cliente models.Cliente

	// Se houver resultado, escaneia os dados do cliente na variável cliente
	if stmt.Next(){
		if err := stmt.Scan(
			&cliente.ID, 
			&cliente.Cpf, 
			&cliente.Nome,
			&cliente.NumeroFilhos, 
			&cliente.EstadoCivil,
			&cliente.Renda,
			&cliente.CreatedAt,
			&cliente.UpdatedAt,
			&cliente.Senha,
		); err != nil {
			return models.Cliente{}, err // Retorna um cliente vazio e o erro se ocorrer um problema na leitura dos dados
		}
	}

	return cliente, nil // Retorna o cliente e nil indicando que não houve erros
}
