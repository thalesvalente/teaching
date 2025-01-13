import { FiSearch, FiArrowLeft } from 'react-icons/fi';
import { RiShutDownLine } from "react-icons/ri";
import { Link } from "react-router-dom";

import { Container, Header, Logout, Search, Label, Content } from './styles';

import { Input } from '../../components/Input';
import { Employee } from '../../components/Employee';

export function Employees () {

  return (
    <Container>

      <Header>
        
        <Link to="/manager">

          <FiArrowLeft />

        </Link>

        <Logout>
          <RiShutDownLine />
        </Logout>

      </Header>

      <Search>
        <Input placeholder="Pesquisar" icon={FiSearch} />
      </Search>

      <Label><h2>Funcionários</h2></Label>

      <Content id="content">

        <Employee data={
          {
            nome : "Diogo Brasil Da Silva",
            id: '12345',
            cargaHoraria: "20hs",
            tempocontrato : "5 anos",
            cargo: "CORRETOR"

          }
        }
        />

      </Content>

    </Container>
  )
}
