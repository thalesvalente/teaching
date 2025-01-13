package main

import (
	"construtora-API/config"       // Importa o pacote config para carregar as configurações da aplicação
	"construtora-API/internal/router" // Importa o pacote router para configurar as rotas da API
	"fmt"                           // Importa o pacote fmt para formatação de saída
)

func main() {
	fmt.Println("Rodando...") // Imprime no console uma mensagem indicando que a aplicação está rodando
	config.Load()               // Chama a função Load do pacote config para carregar as configurações
	router.Initialize()         // Chama a função Initialize do pacote router para configurar as rotas da API
}
