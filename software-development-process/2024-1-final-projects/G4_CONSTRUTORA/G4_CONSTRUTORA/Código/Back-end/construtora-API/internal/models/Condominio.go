package models

import "time"

type Condominio struct {
	ID        uint64    `json:"id"`
	Nome string `json:"nome"`
	QuantidadeImoveis uint64 `json:"quantidade_imoveis"`
	Aminidades string `json:"aminidades"`
	Taxa float64 `json:"taxa"`
	AnoConstrucao uint64 `json:"ano_construcao"`
	Status string `json:"status"`
	IdEndereco uint64 `json:"id_endereco"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	
}

type CondominioInput struct {
	Nome 				string 	  `json:"nome"`
	QuantidadeImoveis   uint64 	  `json:"quantidade_imoveis"`
	Aminidades 			string 	  `json:"aminidades"`
	Taxa 				float64   `json:"taxa"`
	AnoConstrucao   	uint64    `json:"ano_construcao"`
	Status 	  			string 	  `json:"status"`
	Rua       			string    `json:"rua"`
	Numero    			uint64    `json:"numero"`
	Cidade    			string    `json:"cidade"`
	Estado    			string    `json:"estado"`
	Cep       			string    `json:"cep"`
}