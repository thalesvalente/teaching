import { RiShutDownLine } from "react-icons/ri";
import { Link } from 'react-router-dom';

import { Container, Header, Logout, Label, Avatar, Content} from './styles';

export function EmployeeHome() {

  return (
    <Container>
      
      <Header>

        <h1>G4</h1>

        <div>
          <Link to="/imoveis/listar">Listar Imóveis</Link>
          <Link to="#">Listar Condomínio</Link>
          <Link to="/imoveis/cadastrar">Cadastrar Imóvel</Link>
          <Link to="/condominio/cadastrar">Cadastrar Condomínio</Link>
        </div>

        <Logout>
          <RiShutDownLine />
        </Logout>

      </Header>

      <Avatar>

        <img
          src="http://github.com/diogobrasil.png"
          alt="Foto do Usuário"
        />

        <div>
          <span><strong>ID : </strong> 123 </span>
          <strong>Diogo Brasil</strong>
        </div>
      </Avatar>

      <Label><h2>Informações Pessoais</h2></Label>

      <Content id="content">

      <dl>
          <dt>Nome Completo</dt>
          <dd>Diogo Brasil Da Silva</dd>

          <dt>Nº CPF</dt>
          <dd>02203304405</dd>

          <dt>Cargo</dt>
          <dd>Serviços Gerais</dd>

          <dt>Carga Horária</dt>
          <dd>20hs</dd>

          <dt>Estado Civil</dt>
          <dd>Solteiro</dd>
          
          <dt>Renda</dt>
          <dd>R$ 2500.00</dd>
        </dl>

      </Content>

    </Container>
  )
}
