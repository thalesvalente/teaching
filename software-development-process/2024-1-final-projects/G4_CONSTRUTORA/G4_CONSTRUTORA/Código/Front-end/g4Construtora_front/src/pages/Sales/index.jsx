import { FiSearch, FiArrowLeft } from 'react-icons/fi';
import { RiShutDownLine } from "react-icons/ri";
import { Link } from 'react-router-dom';

import { Container, Header, Logout, Search, Label, Content } from './styles';

import { Input } from '../../components/Input';
import { Sale } from '../../components/Sale';

// Componente de visualização de vendas

export function Sales() {

  return (
    <Container>

      <Header>

        <Link to="/">

          <FiArrowLeft />

        </Link>

        <Logout>
          <RiShutDownLine />
        </Logout>

      </Header>

      <Search>
        <Input placeholder="Pesquisar" icon={FiSearch} />
      </Search>

      <Label><h2>Vendas</h2></Label>

      <Content id="content">
        {/* Componente Sale que exibe os detalhes de uma venda específica */}
        <Sale data={
          {
            id: '12345',
            descricao: 'Casa de dois andares, com varanda e vista para o mar. Ótima para criar os filhos, convidar a família e amigos para um churrascos. Vizinhos tranquilos e gentis.',
            status: "EM ANDAMENTO"
          }
        }
        />

      </Content>

    </Container>
  )
}
