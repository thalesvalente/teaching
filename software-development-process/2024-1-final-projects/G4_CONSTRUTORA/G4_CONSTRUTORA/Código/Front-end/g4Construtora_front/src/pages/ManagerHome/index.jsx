import { FiPlus } from 'react-icons/fi';
import { RiShutDownLine } from "react-icons/ri";

import { Container, Header, Logout, Brand, Menu, Label, Avatar, Content, Create, CreateEmployee, Cond } from './styles';

import { ButtonText } from '../../components/ButtonText';
import { useAuth } from '../../hook/auth';



export function ManagerHome() {
  const {signOut} = useAuth()
  return (
    <Container>
      <Brand>
        <h2>
          G4
        </h2>
      </Brand>

      <Header>

        <Logout onClick={signOut}>
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

        <li>
          <ButtonText title="Funcionários" to="/funcionario/listar" />
        </li>

        <li>
          <ButtonText title="Relatório de Vendas" to="#" />
        </li>

      </Menu>

      <Avatar>

        <img
          src="https://i.pinimg.com/originals/9e/33/ba/9e33ba72072e0f010eeccfe5df621500.jpg"
          alt="Foto do Usuário"
        />

        <div>
          <span><strong>ID : </strong> 123 </span>
          <strong>Beckham</strong>
        </div>
      </Avatar>

      <Label><h2>Informações Pessoais</h2></Label>

      <Content id="content">

      <dl>
          <dt>Nome Completo</dt>
          <dd>Guilherme Beckham</dd>

          <dt>Nº CPF</dt>
          <dd>02203304405</dd>

          <dt>Cargo</dt>
          <dd>Gerente</dd>

          <dt>Carga Horária</dt>
          <dd>20hs</dd>

          <dt>Estado Civil</dt>
          <dd>Solteiro</dd>
          
          <dt>Renda</dt>
          <dd>R$ 2500.00</dd>
        </dl>

      </Content>


      <Create to="/imoveis/cadastrar">
        <FiPlus />
        Cadastrar Imóvel
      </Create>

      <CreateEmployee to="/funcionario/cadastrar">
        <FiPlus />
        Cadastrar Funcionário
      </CreateEmployee>

      <Cond to="/condominio/cadastrar">
        <FiPlus />
        Cadastrar Condomínio
      </Cond>

    </Container>
  )
}
