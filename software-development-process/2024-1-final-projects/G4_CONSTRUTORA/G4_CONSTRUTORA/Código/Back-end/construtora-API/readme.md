# G4 - API de Cadastro de Imóveis

Bem-vindo à documentação da API G4, um sistema de cadastro de imóveis desenvolvido em Golang. Esta API oferece uma maneira simples e eficiente de gerenciar informações sobre imóveis e funcionários, incluindo sua localização, características e outros detalhes relevantes.

## Recursos Principais

1. **Cadastro de Imóveis:** Registre novos imóveis especificando detalhes como endereço, tipo de imóvel, número de quartos, etc.
2. **Consulta de Imóveis:** Recupere informações detalhadas sobre imóveis cadastrados com base em critérios específicos.
3. **Atualização e Exclusão:** Atualize ou remova imóveis existentes conforme necessário.
4. **Cadastro e Gerência de Funcionários:** Cadastre e Gerencie funcionários com cargos e funcionalidades definidas
5. **Cadastro e Gerência de clientes:** Cadastre e Gerencie clientes.

## Endpoints Disponíveis

- **POST /login:** Garante acesso ao sistema dadas as credenciais do funcionário ou cliente

- **POST /funcionario/cadastro:** Cria um novo registro de funcionário com os detalhes fornecidos.
- **POST /funcionario/atualizar/{id}:** Atualiza um registro de funcionário já existente no banco.
- **GET /funcionario/todos:** Lista todos os funcionários.

- **POST /cliente/cadastrar:** Cria um novo registro de cliente com os detalhes fornecidos.
- **GET /cliente/listar:** Lista todos os clientes

- **POST /imovel/cadastrar:** Cria um novo registro de imóvel com os detalhes fornecidos.
- **POST /imovel/listar:** Lista todos os imóveis.
- **POST /imovel/buscar/{id}:** Busca um imóvel específico.

## Instalação e Uso

1. Certifique-se de ter o Go instalado em sua máquina. Para instalar o Go, consulte [a documentação oficial](https://golang.org/doc/install).
2. Clone este repositório para o seu ambiente local.
3. Navegue até o diretório `/cmd/api/` do projeto e execute o comando `go build` para compilar o código.
4. Após a compilação bem-sucedida, execute o arquivo `api.exe` executável gerado.
5. A API estará disponível em `http://localhost:8080` por padrão.
