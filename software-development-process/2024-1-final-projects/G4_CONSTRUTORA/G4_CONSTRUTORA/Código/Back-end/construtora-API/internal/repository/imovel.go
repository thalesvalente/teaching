package repository

import (
	"construtora-API/internal/models" // Importa o pacote onde os modelos de dados são definidos
	"database/sql"                    // Importa o pacote de SQL que fornece uma interface genérica para banco de dados
)

// Imovel é uma struct que contém uma referência ao banco de dados
type Imovel struct {
	db *sql.DB
}

// NovoRepositorioImovel cria um novo repositório de imóveis com uma conexão ao banco de dados
func NovoRepositorioImovel(db *sql.DB) *Imovel {
	return &Imovel{db} // Retorna um ponteiro para Imovel com a conexão ao banco de dados
}

// CadastrarImovel insere um novo imóvel no banco de dados e retorna o imóvel inserido
func (i *Imovel) CadastrarImovel(imovel models.Imovel) (models.Imovel, error) {
	sql := "INSERT INTO Imoveis (tipo, preco, area_total, estado, num_quartos, num_banheiros, id_condominio) VALUES ($1, $2, $3, $4, $5, $6, $7)"

	// Prepara a instrução SQL para execução
	stmt, err := i.db.Prepare(sql)
	if err != nil {
		return models.Imovel{}, err // Retorna um imóvel vazio e o erro se ocorrer um problema na preparação da instrução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	// Executa a instrução SQL com os dados do imóvel
	_, err = stmt.Exec(imovel.Tipo, imovel.Preco, imovel.AreaTotal, imovel.Estado, imovel.NumQuartos, imovel.NumBanheiros, imovel.IdCondominio)
	if err != nil {
		return models.Imovel{}, err // Retorna um imóvel vazio e o erro se ocorrer um problema na execução
	}

	return imovel, nil // Retorna o imóvel e nil indicando que não houve erros
}

// ListarTodosImoveis retorna uma lista de todos os imóveis do banco de dados com informações adicionais do condomínio e endereço
func (i *Imovel) ListarTodosImoveis() ([]models.ImovelResponse, error) {
	sql := "SELECT i.id, i.tipo, i.preco, i.area_total, i.estado AS imovel_estado, i.num_quartos, i.num_banheiros, c.nome, c.quantidade_imoveis, c.aminidades, c.taxa, c.ano_construcao, c.status, e.rua, e.numero, e.cidade, e.estado, e.cep " +
		"FROM imoveis i " +
		"JOIN condominios c ON i.id_condominio = c.id " +
		"JOIN enderecos e ON c.id_endereco = e.id"

	// Executa a instrução SQL para selecionar todos os imóveis com dados adicionais
	stmt, err := i.db.Query(sql)
	if err != nil {
		return nil, err // Retorna nil e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var imoveis []models.ImovelResponse

	// Itera sobre os resultados da consulta
	for stmt.Next() {
		var imovel models.ImovelResponse
		// Escaneia os dados do imóvel na variável imovel
		if err = stmt.Scan(
			&imovel.ID,
			&imovel.Tipo,
			&imovel.Preco,
			&imovel.AreaTotal,
			&imovel.ImovelEstado,
			&imovel.NumQuartos,
			&imovel.NumBanheiros,
			&imovel.Nome,
			&imovel.QuantidadeImoveis,
			&imovel.Aminidades,
			&imovel.Taxa,
			&imovel.AnoConstrucao,
			&imovel.Status,
			&imovel.Rua,
			&imovel.Numero,
			&imovel.Cidade,
			&imovel.Estado,
			&imovel.Cep,
		); err != nil {
			return nil, err // Retorna nil e o erro se ocorrer um problema na leitura dos dados
		}

		imoveis = append(imoveis, imovel) // Adiciona o imóvel na lista de imóveis
	}

	return imoveis, nil // Retorna a lista de imóveis e nil indicando que não houve erros
}

// BuscarPorId busca um imóvel no banco de dados pelo ID e retorna seus detalhes com informações adicionais do condomínio e endereço
func (i *Imovel) BuscarPorId(id uint64) (models.ImovelResponse, error) {
	sql := "SELECT i.id, i.tipo, i.preco, i.area_total, i.estado AS imovel_estado, i.num_quartos, i.num_banheiros, c.nome, c.quantidade_imoveis, c.aminidades, c.taxa, c.ano_construcao, c.status, e.rua, e.numero, e.cidade, e.estado, e.cep " +
		"FROM imoveis i " +
		"JOIN condominios c ON i.id_condominio = c.id " +
		"JOIN enderecos e ON c.id_endereco = e.id " +
		"WHERE i.id = $1"

	// Executa a instrução SQL para selecionar o imóvel pelo ID
	stmt, err := i.db.Query(sql, id)
	if err != nil {
		return models.ImovelResponse{}, err // Retorna um imóvel vazio e o erro se ocorrer um problema na execução
	}
	defer stmt.Close() // Garante que o statement será fechado após a execução

	var imovel models.ImovelResponse

	// Se houver resultado, escaneia os dados do imóvel na variável imovel
	if stmt.Next() {
		if err := stmt.Scan(
			&imovel.ID,
			&imovel.Tipo,
			&imovel.Preco,
			&imovel.AreaTotal,
			&imovel.ImovelEstado,
			&imovel.NumQuartos,
			&imovel.NumBanheiros,
			&imovel.Nome,
			&imovel.QuantidadeImoveis,
			&imovel.Aminidades,
			&imovel.Taxa,
			&imovel.AnoConstrucao,
			&imovel.Status,
			&imovel.Rua,
			&imovel.Numero,
			&imovel.Cidade,
			&imovel.Estado,
			&imovel.Cep,
		); err != nil {
			return models.ImovelResponse{}, err // Retorna um imóvel vazio e o erro se ocorrer um problema na leitura dos dados
		}
	}

	return imovel, nil // Retorna o imóvel e nil indicando que não houve erros
}
