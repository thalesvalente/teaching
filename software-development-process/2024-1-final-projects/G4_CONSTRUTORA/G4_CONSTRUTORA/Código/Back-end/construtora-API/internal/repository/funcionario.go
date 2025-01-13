package repository

import (
	"construtora-API/internal/models" // Importa o pacote onde os modelos de dados são definidos
	"database/sql"                    // Importa o pacote de SQL que fornece uma interface genérica para banco de dados
)

// Funcionario é uma struct que contém uma referência ao banco de dados
type Funcionario struct {
	db *sql.DB
}

// NovoRepositorioFuncionario cria um novo repositório de funcionários com uma conexão ao banco de dados
func NovoRepositorioFuncionario(db *sql.DB) *Funcionario {
	return &Funcionario{db} // Retorna um ponteiro para Funcionario com a conexão ao banco de dados
}

// CadastrarFuncionario insere um novo funcionário no banco de dados e retorna o funcionário inserido
func (f *Funcionario) CadastrarFuncionario(Funcionario models.Funcionario) (models.Funcionario, error) {
	sql := "INSERT INTO Funcionarios (nome, cpf, numero_de_filhos, estado_civil, renda, data_pagamento, carga_horaria, creci, funcao, password) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)"

	// Prepara a instrução SQL para execução
	stmt, err := f.db.Prepare(sql)
	if err != nil {
		return models.Funcionario{}, err // Retorna um funcionário vazio e o erro se ocorrer um problema na preparação da instrução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	// Executa a instrução SQL com os dados do funcionário
	_, err = stmt.Exec(Funcionario.Nome, Funcionario.Cpf, Funcionario.NumeroFilhos, Funcionario.EstadoCivil, Funcionario.Renda, Funcionario.DataPagamento, Funcionario.CargaHoraria, Funcionario.Creci, Funcionario.Funcao, Funcionario.Password)
	if err != nil {
		return models.Funcionario{}, err // Retorna um funcionário vazio e o erro se ocorrer um problema na execução
	}

	return Funcionario, err // Retorna o funcionário e nil indicando que não houve erros
}

// ListarTodosFuncionarios retorna uma lista de todos os funcionários do banco de dados
func (f *Funcionario) ListarTodosFuncionarios() ([]models.Funcionario, error) {
	query := "SELECT * from Funcionarios"

	// Executa a instrução SQL para selecionar todos os funcionários
	stmt, err := f.db.Query(query)
	if err != nil {
		return nil, err // Retorna nil e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var funcionarios []models.Funcionario
	var creci sql.NullInt64 // Variável para armazenar o valor do campo creci que pode ser nulo

	// Itera sobre os resultados da consulta
	for stmt.Next() {
		var funcionario models.Funcionario
		// Escaneia os dados do funcionário na variável funcionario
		if err = stmt.Scan(
			&funcionario.ID,
			&funcionario.Nome,
			&funcionario.Cpf,
			&funcionario.NumeroFilhos, 
			&funcionario.EstadoCivil, 
			&funcionario.Renda,
			&funcionario.DataPagamento,
			&funcionario.CargaHoraria,
			&creci,
			&funcionario.Password,
			&funcionario.CreatedAt,
			&funcionario.UpdatedAt,
			&funcionario.Funcao,
		); err != nil {
			return nil, err // Retorna nil e o erro se ocorrer um problema na leitura dos dados
		}

		// Atribui o valor do campo creci ao funcionário, se não for nulo
		if creci.Valid {
			funcionario.Creci = creci.Int64
		}

		funcionarios = append(funcionarios, funcionario) // Adiciona o funcionário na lista de funcionários
	}

	return funcionarios, nil // Retorna a lista de funcionários e nil indicando que não houve erros
}

// AtualizarFuncionario atualiza os dados de um funcionário no banco de dados
func (f *Funcionario) AtualizarFuncionario(Funcionario models.Funcionario) error {
	sql := "UPDATE Funcionarios set nome = $1, cpf = $2, numero_de_filhos = $3, estado_civil = $4, renda = $5, data_pagamento = $6, carga_horaria = $7, creci = $8, funcao = $9, password = $10 WHERE id = $11"

	// Prepara a instrução SQL para execução
	stmt, err := f.db.Prepare(sql)
	if err != nil {
		return err // Retorna o erro se ocorrer um problema na preparação da instrução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	// Executa a instrução SQL com os dados atualizados do funcionário
	_, err = stmt.Exec(Funcionario.Nome, Funcionario.Cpf, Funcionario.NumeroFilhos, Funcionario.EstadoCivil, Funcionario.Renda, Funcionario.DataPagamento, Funcionario.CargaHoraria, Funcionario.Creci, Funcionario.Funcao, Funcionario.Password, Funcionario.ID)
	if err != nil {
		return err // Retorna o erro se ocorrer um problema na execução
	}

	return nil // Retorna nil indicando que não houve erros
}

// BuscarPorCPF busca um funcionário no banco de dados pelo CPF
func (f *Funcionario) BuscarPorCPF(cpf string) (models.Funcionario, error) {
	query := "SELECT * FROM Funcionarios where cpf = $1"

	// Executa a instrução SQL para selecionar o funcionário pelo CPF
	stmt, err := f.db.Query(query, cpf)
	if err != nil {
		return models.Funcionario{}, err // Retorna um funcionário vazio e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var funcionario models.Funcionario
	var creci sql.NullInt64 // Variável para armazenar o valor do campo creci que pode ser nulo

	// Se houver resultado, escaneia os dados do funcionário na variável funcionario
	if stmt.Next() {
		if err := stmt.Scan(
			&funcionario.ID,
			&funcionario.Nome,
			&funcionario.Cpf,
			&funcionario.NumeroFilhos, 
			&funcionario.EstadoCivil, 
			&funcionario.Renda,
			&funcionario.DataPagamento,
			&funcionario.CargaHoraria,
			&creci,
			&funcionario.Password,
			&funcionario.CreatedAt,
			&funcionario.UpdatedAt,
			&funcionario.Funcao,
		); err != nil {
			return models.Funcionario{}, err // Retorna um funcionário vazio e o erro se ocorrer um problema na leitura dos dados
		}

		// Atribui o valor do campo creci ao funcionário, se não for nulo
		if creci.Valid {
			funcionario.Creci = creci.Int64
		}
	}

	return funcionario, nil // Retorna o funcionário e nil indicando que não houve erros
}
