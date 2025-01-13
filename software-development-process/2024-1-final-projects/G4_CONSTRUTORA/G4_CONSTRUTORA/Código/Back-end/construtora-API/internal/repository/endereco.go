package repository

import (
	"database/sql"    // Importa o pacote de SQL que fornece uma interface genérica para banco de dados
	"errors"          // Importa o pacote de errors para manipulação de erros
)

// Endereco é uma struct que contém uma referência ao banco de dados
type Endereco struct {
	db *sql.DB
}

// NovoRepositorioEndereco cria um novo repositório de endereços com uma conexão ao banco de dados
func NovoRepositorioEndereco(db *sql.DB) *Endereco {
	return &Endereco{db} // Retorna um ponteiro para Endereco com a conexão ao banco de dados
}

// CadastrarEndereco insere um novo endereço no banco de dados e retorna o ID do endereço inserido
func (e *Endereco) CadastrarEndereco(rua string, numero uint64, cidade, estado, cep string) (int64, error) {

	var ultimoId int64
	sql := "INSERT INTO Enderecos (rua, numero, cidade, estado, cep) VALUES($1, $2, $3, $4, $5) RETURNING id"

	// Executa a instrução SQL para inserir o endereço e retorna o ID do novo registro
	err := e.db.QueryRow(sql, rua, numero, cidade, estado, cep).Scan(&ultimoId)
	if err != nil {
		return 0, errors.New("error querying enderecos") // Retorna 0 e uma mensagem de erro se ocorrer um problema na execução
	}

	return ultimoId, nil // Retorna o ID do endereço inserido e nil indicando que não houve erros
}
