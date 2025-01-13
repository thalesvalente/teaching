import { FiArrowLeft } from "react-icons/fi";
import { RiShutDownLine } from "react-icons/ri";
import { Link } from "react-router-dom";

import { Button } from "../../components/Button";

import { Container, Header, Logout, Content } from "./styles";

export function DetailsProperty() {

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

      <main>
        <Content>

          <div>

            <img
              src="https://plus.unsplash.com/premium_photo-1687960117069-567a456fe5f3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              alt="foto da propriedade"
            />

          </div>

          <section><h2>Dados do Imóvel</h2></section>

          <dl>
            <dt>ID</dt>
            <dd>12345</dd>
            <dt>Tipo</dt>
            <dd>Casa</dd>
            <dt>Condomínio</dt>
            <dd>Paraty</dd>
            <dt>Status</dt>
            <dd>Disponível</dd>
            <dt>Nº de Quartos</dt>
            <dd>5 Quartos</dd>
            <dt>Nº de Banheiros</dt>
            <dd>2</dd>
            <dt>Preço</dt>
            <dd>R$ 12.756,99</dd>
            <dt>Endereço</dt>
            <dd>Rua Das Flores, 20, São Luís, 67450-000</dd>
          </dl>
          
          <div className="buttons">

            <Button title="Editar" />
            <Button title="Excluir" />

          </div>

        </Content>

      </main>

    </Container>
  )
}
