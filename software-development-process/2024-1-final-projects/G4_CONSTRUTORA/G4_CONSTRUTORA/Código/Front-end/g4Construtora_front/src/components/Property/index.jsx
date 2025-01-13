import { Container, Image, AboutProperty } from './styles';
import { CiMap } from "react-icons/ci";
import { FaMapMarkedAlt } from "react-icons/fa";

import { Status } from '../../components/Status';

// Este componente exibe informações sobre uma propriedade, incluindo nome, descrição,
//  * endereço e status. Inclui também uma imagem representativa da propriedade.

export function Property ({ data, ...rest}) {
  return (
    <Container {...rest}>
      <AboutProperty>

         <div className='titulo'>
            <h1>{data.nome}</h1>
            <p>{data.descricao}</p>
          </div> 

          <div className='endereco'>
            <FaMapMarkedAlt/>
            <p> {data.endereco.cidade}, {data.endereco.estado} </p>
            <p> {data.endereco.rua}, {data.endereco.cep}</p>
          </div>

          { 
            data.status &&
              <footer>
                <Status title={data.status} sold={String(data.status).toLocaleLowerCase() === "disponível" ? true : false }/>
              </footer>
          }
      
      </AboutProperty>
       
        <Image
          src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        />
          
    
    </Container>
  )
}
