package repository

import (
	"construtora-API/internal/models" // Importa o pacote onde os modelos de dados são definidos
	"database/sql"                    // Importa o pacote de SQL que fornece uma interface genérica para banco de dados
)

// Condominio é uma struct que contém uma referência ao banco de dados
type Condominio struct {
	db *sql.DB
}

// NovoRepositorioCondominio cria um novo repositório de condomínios com uma conexão ao banco de dados
func NovoRepositorioCondominio(db *sql.DB) *Condominio {
	return &Condominio{db} // Retorna um ponteiro para Condominio com a conexão ao banco de dados
}

// CadastrarCondominio insere um novo condomínio no banco de dados
func (c *Condominio) CadastrarCondominio(nome string, quantidadeImoveis uint64, aminidades string, taxa float64, anoConstrucao uint64, status string, idEndereco int64) error {

	sql := "INSERT INTO Condominios (nome, quantidade_imoveis, aminidades, taxa, ano_construcao, status, id_endereco) VALUES ($1, $2, $3, $4, $5, $6, $7)"

	// Prepara a instrução SQL para execução
	stmt, err := c.db.Prepare(sql)
	if err != nil {
		return err // Retorna o erro se ocorrer um problema na preparação da instrução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	// Executa a instrução SQL com os dados do condomínio
	_, err = stmt.Exec(nome, quantidadeImoveis, aminidades, taxa, anoConstrucao, status, idEndereco)
	if err != nil {
		return err // Retorna o erro se ocorrer um problema na execução
	}

	return nil // Retorna nil indicando que não houve erros
}

// ListarTodosCondominios retorna uma lista de todos os condomínios do banco de dados
func (c *Condominio) ListarTodosCondominios()([]models.Condominio, error) {
	sql := "SELECT * FROM Condominios"

	// Executa a instrução SQL para selecionar todos os condomínios
	stmt, err := c.db.Query(sql)
	if err != nil {
		return nil, err // Retorna nil e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var condominios []models.Condominio

	// Itera sobre os resultados da consulta
	for stmt.Next() {
		var condominio models.Condominio
		// Escaneia os dados do condomínio na variável condominio
		if err = stmt.Scan(
			&condominio.ID,
			&condominio.Nome,
			&condominio.QuantidadeImoveis,
			&condominio.Aminidades,
			&condominio.Taxa,
			&condominio.AnoConstrucao,
			&condominio.Status,
			&condominio.IdEndereco,
			&condominio.CreatedAt,
			&condominio.UpdatedAt,
		); err != nil {
			return nil, err // Retorna nil e o erro se ocorrer um problema na leitura dos dados
		}

		condominios = append(condominios, condominio) // Adiciona o condomínio na lista de condomínios
	}

	return condominios, nil // Retorna a lista de condomínios e nil indicando que não houve erros
}
