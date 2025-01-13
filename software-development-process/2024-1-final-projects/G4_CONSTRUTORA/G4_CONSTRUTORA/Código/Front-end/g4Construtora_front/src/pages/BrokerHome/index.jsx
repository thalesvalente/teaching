import { FiPlus} from 'react-icons/fi';
import { RiShutDownLine } from "react-icons/ri";

import { Container, Header, Logout, Brand, Menu, Avatar, Label, Content, Create, Cond } from './styles';

import { ButtonText } from '../../components/ButtonText';

export function BrokerHome() {

  return (
    <Container>
      <Brand>
        <h2>
          G4
        </h2>
      </Brand>

      <Header>

        <Logout>
          <RiShutDownLine />
        </Logout>

      </Header>

      <Menu>

        <li>
          <ButtonText title="Imóveis" to="/imoveis/listar" />
        </li>

        <li>
          <ButtonText title="Vendas" to="/vendas" />
        </li>

      </Menu>

      <Avatar>

        <img
          src="http://github.com/matheus2049alves.png"
          alt="Foto do Usuário"
        />

        <div>
          <span><strong>ID : </strong> 123 </span>
          <strong>Matheus</strong>
        </div>
      </Avatar>

      <Label><h2>Informações Pessoais</h2></Label>

      <Content id="content">

        <dl>
          <dt>Nome Completo</dt>
          <dd>Matheus Costa Alves</dd>

          <dt>Nº CPF</dt>
          <dd>02203304405</dd>

          <dt>Cargo</dt>
          <dd>Corretor</dd>

          <dt>Carga Horária</dt>
          <dd>20hs</dd>

          <dt>Estado Civil</dt>
          <dd>Solteiro</dd>
          
          <dt>Renda</dt>
          <dd>R$ 2500.00</dd>
        </dl>

      </Content>

      <Cond to="/condominio/cadastrar">
        <FiPlus />
        Cadastrar Condomínio
      </Cond>

      <Create to="/imoveis/cadastrar">
        <FiPlus />
        Cadastrar Imóvel
      </Create>

    </Container>
  )
}
