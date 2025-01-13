package models

import "time"

type Imovel struct {
	ID           uint64    `json:"id"`
	Tipo         string    `json:"tipo"`
	Preco        uint64    `json:"preco"`
	AreaTotal    uint64    `json:"area_total"`
	Estado       string    `json:"estado"`
	NumQuartos   uint64    `json:"num_quartos"`
	NumBanheiros uint64    `json:"num_banheiros"`
	IdCondominio uint64    `json:"id_condominio"`
	CreatedAt    time.Time `json:"created_at"`
	UpdatedAt    time.Time `json:"updated_at"`
}

type ImovelResponse struct {
	ID 				  uint64 	`json:"id"`
	Tipo         	  string    `json:"tipo"`
	Preco        	  uint64    `json:"preco"`
	AreaTotal    	  uint64    `json:"area_total"`
	ImovelEstado      string    `json:"imovel_estado"`
	NumQuartos   	  uint64    `json:"num_quartos"`
	NumBanheiros 	  uint64    `json:"num_banheiros"`
	Nome 			  string 	`json:"nome"`
	QuantidadeImoveis uint64 	`json:"quantidade_imoveis"`
	Aminidades 		  string 	`json:"aminidades"`
	Taxa 		 	  float64 	`json:"taxa"`
	AnoConstrucao 	  uint64 	`json:"ano_construcao"`
	Status 			  string 	`json:"status"`
	Rua       		  string    `json:"rua"`
	Numero    		  uint64    `json:"numero"`
	Cidade    		  string    `json:"cidade"`
	Estado    		  string    `json:"estado"`
	Cep      		  string    `json:"cep"`
}

