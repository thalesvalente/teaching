package models

import "time"

type Cliente struct {
	ID           uint64    `json:"id"`
	Cpf          string    `json:"cpf"`
	Nome         string    `json:"nome"`
	NumeroFilhos uint64    `json:"numero_de_filhos"`
	EstadoCivil  string    `json:"estado_civil"`
	Renda        uint64    `json:"renda"`
	Senha 		 string	   `json:"senha"`
	CreatedAt    time.Time `json:"created_at"`
	UpdatedAt    time.Time `json:"updated_at"`
}