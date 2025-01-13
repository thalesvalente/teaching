CREATE TABLE Funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    numero_de_filhos integer NOT NULL,
    estado_civil VARCHAR(20) NOT NULL,
   	renda integer NOT NULL,
   	data_pagamento TIMESTAMP NOT NULL,
   	carga_horaria decimal NOT NULL,
   	creci smallint,
    funcao varchar(20) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table Clientes (
	id SERIAL PRIMARY KEY,
	cpf VARCHAR(11) NOT NULL,
	nome VARCHAR(100) NOT NULL,
	numero_de_filhos integer NOT NULL,
    estado_civil VARCHAR(20) NOT NULL,
   	renda integer NOT null,
   	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


create table Enderecos(
	id serial primary key,
	rua varchar(30) not null, 
	numero smallint not null,
	cidade varchar(30) not null,
	estado varchar(30) not null,
	cep varchar(8) not null,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

create table Condominios (
	id serial primary key,
	nome VARCHAR(100) NOT NULL,
	quantidade_imoveis smallint not null,
	aminidades text,
	taxa numeric not null,
	ano_construcao smallint not null,
	status varchar(20),
	id_endereco INTEGER REFERENCES Enderecos(id) ON DELETE cascade,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)


create table Imoveis (
	id SERIAL primary key,
	tipo varchar(20) not null, 
	preco numeric not null,
	area_total numeric not null,
	estado varchar(20) not null,
	num_quartos smallint not null, 
	num_banheiros smallint not null,
	id_condominio INTEGER REFERENCES Condominios(id) ON DELETE CASCADE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	
)

create table Vendas (
	data_inicio TIMESTAMP default current_timestamp,
	data_fim TIMESTAMP,
	status VARCHAR(20) NOT null, 
	id_funcionario INTEGER REFERENCES Funcionarios(id) ON DELETE CASCADE,
	id_cliente INTEGER REFERENCES Clientes(id) ON DELETE CASCADE,
	id_imovel INTEGER REFERENCES Imoveis(id) ON DELETE CASCADE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)