import { Container,Details, AboutProperty} from "./styles";
import { Button } from "../../components/Button";
import {Header} from "../../components/Header"
import { useParams } from "react-router-dom";
import { useEffect , useState} from "react";
import { api } from "../../services/api";
import { MdBathroom } from "react-icons/md";

// Componente que exibe os detalhes de uma propriedade
export function PropertyDetails(){
  const {id} = useParams() // Obtém o ID da propriedade a partir dos parâmetros da URL
  const [property, setProperty] = useState(""); // Estado para armazenar os dados da propriedade

  useEffect(() => {
    // Função assíncrona para buscar os detalhes da propriedade a partir da API
    async function fetchProperties() {
      try {
        const response = await api.get(`/imovel/buscar/${id}`);
        const {imovel} = response.data
        setProperty(imovel) // Atualiza o estado com os dados da propriedade
      } catch (error) {
        if (error){
          alert(error.response.data.message)
        }
        console.error("Erro ao buscar imóveis:", error);
      }
    }

    
  
    fetchProperties();  // Chama a função de busca ao montar o componente
  }, [id]); // Dependência do efeito: reexecuta quando o ID da propriedade mudar
  console.log(property)
  

  return(
    <Container>
      <Header/>
      <Details>
        <img 
        src="https://plus.unsplash.com/premium_photo-1687960117069-567a456fe5f3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
         alt="foto da propriedade" 
         />
        {/* Informações principais da propriedade */}
         <div className="NameInformation">
          <p>{property.cidade}</p>
          <h2>{property.nome}</h2>
         </div>
          {/* Caixa de solicitação de compra */}
        <div className="PurchaseBox">
          <p>Ficou interpresado?</p>
          <Button title={" Solicitar Compra"}/>
        </div>
         {/* Detalhes sobre a propriedade */}
        <AboutProperty>
          <h2>Detalhes do imóvel</h2>
          <dl>
            <dt>Nome do condomínio</dt>
            <dd>{property.nome}</dd>
            <dt>Tipo de imóvel</dt>
            <dd>{property.tipo}</dd>
            <dt>Área do imóvel</dt>
          <dd>{`${property.area_total} m²`}</dd>
            <dt>Estado do imóvel</dt>
            <dd>{property.imovel_estado}</dd>
            <dt>Número de quartos</dt>
            <dd>{property.num_quartos}</dd>
            <dt>Número de banheiros {<MdBathroom/>}</dt>
            <dd>{property.num_banheiros}</dd>
          </dl>

        </AboutProperty>
      </Details>
    </Container>
  )
}