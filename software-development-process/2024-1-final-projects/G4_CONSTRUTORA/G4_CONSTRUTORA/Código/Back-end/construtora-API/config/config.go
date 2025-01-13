package config

import (
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
)

var (
	ConnectDBUrl = "" // ConnectDBUrl é uma variável global que armazenará a string de conexão com o banco de dados
)

func Load() {
	var err error
	
	// Carrega as variáveis de ambiente do arquivo .env na raiz do projeto
	if err = godotenv.Load(); err != nil {
		log.Fatal(err) // Se houver erro ao carregar o arquivo .env, encerra a aplicação e imprime o erro
	}

	// Constrói a string de conexão com o banco de dados usando os valores do arquivo .env
	ConnectDBUrl = fmt.Sprintf("host=%s port=%s user=%s dbname=%s password=%s sslmode=disable",
		os.Getenv("DB_HOST"),    // Obtém o valor da variável de ambiente DB_HOST
		os.Getenv("DB_PORT"),    // Obtém o valor da variável de ambiente DB_PORT
		os.Getenv("DB_USER"),    // Obtém o valor da variável de ambiente DB_USER
		os.Getenv("DB_NAME"),    // Obtém o valor da variável de ambiente DB_NAME
		os.Getenv("DB_PASSWORD"),// Obtém o valor da variável de ambiente DB_PASSWORD
	)
}
