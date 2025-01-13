package database

import (
	"construtora-API/config" // Importa o pacote de configuração onde as configurações do banco de dados são armazenadas
	"database/sql"           // Importa o pacote de SQL que fornece uma interface genérica para banco de dados

	_ "github.com/lib/pq"    // Importa a biblioteca do driver Postgres sem usá-la diretamente, só para registro
)

// ConnectDB é uma função que conecta ao banco de dados PostgreSQL e retorna um objeto de conexão (*sql.DB) ou um erro
func ConnectDB() (*sql.DB, error) {
	// Abre uma conexão com o banco de dados utilizando a URL de conexão fornecida na configuração
	db, err := sql.Open("postgres", config.ConnectDBUrl)
	if err != nil {
		// Retorna nil e o erro se ocorrer um problema ao abrir a conexão
		return nil, err
	}

	// Verifica se a conexão com o banco de dados está ativa
	if err := db.Ping(); err != nil {
		// Fecha a conexão se o ping falhar e retorna nil e o erro
		db.Close()
		return nil, err
	}
	// Retorna o objeto de conexão do banco de dados e nil indicando que não houve erros
	return db, nil
}
