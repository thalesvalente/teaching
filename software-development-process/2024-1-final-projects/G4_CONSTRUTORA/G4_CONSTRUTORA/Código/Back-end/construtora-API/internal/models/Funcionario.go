package models

import "time"

type Funcionario struct {
	ID            uint64 `json:"id"`
	Nome          string `json:"nome"`
	Cpf           string `json:"cpf"`
	NumeroFilhos  uint64 `json:"numero_de_filhos"`
	EstadoCivil   string `json:"estado_civil"`
	Renda         uint64 `json:"renda"`
	DataPagamento string `json:"data_pagamento"`
	CargaHoraria float64 `json:"carga_horaria"`
	Creci int64 `json:"creci"`
	Funcao string `json:"funcao"`
	Password string `json:"password"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}