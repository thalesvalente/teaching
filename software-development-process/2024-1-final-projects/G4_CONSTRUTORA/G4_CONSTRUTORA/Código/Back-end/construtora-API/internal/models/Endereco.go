package models

import "time"

type Endereco struct {
	ID        uint64    `json:"id"`
	Rua       string    `json:"rua"`
	Numero    uint64    `json:"numero"`
	Cidade    string    `json:"cidade"`
	Estado    string    `json:"estado"`
	Cep       string    `json:"cep"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}
