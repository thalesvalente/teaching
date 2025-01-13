import { Container, Filter, Slider,Footer} from "./styles";
import { PropertyCard } from "../../components/PropertyCard";
import {Header} from "../../components/Header";
import { Swiper, SwiperSlide } from 'swiper/react';
import {Pagination,Autoplay} from "swiper/modules"
import 'swiper/css';
import 'swiper/css/pagination';
import { api } from "../../services/api";
import { useEffect, useState } from "react";


export function ClientHome() {
  //busaca cos dados de imóveis
  const [property, setProperty] = useState([]);
  useEffect(() => {
    async function fetchProperties() {
      try {
        const response = await api.get("/imovel/listar");
        setProperty(response.data.imoveis);
      } catch (error) {
        if (error){
          alert(error.response.data.message)
        }
        console.error("Erro ao buscar imóveis:", error);
      }
    }
  
    fetchProperties(); 
  }, []); 

  return (
    <Container>
      <Header/>
      <Filter/>
      <Slider>
        <div><h2>Destaques para você</h2></div>
        {/* {exibe um slide que mostra os imóveis com suas informações} */}
        <Swiper
          modules={[Pagination, Autoplay]}
          spaceBetween={50} //espaços entre os slides
          slidesPerView={3}
          pagination={{ clickable: true }} //exibe indicadores onde os usuarios clicam para passar de slide
          autoplay={{
            delay: 3000,
            disableOnInteraction: false, //O autoplay continuará mesmo após a interação do usuário.
          }}
        >
          {property.map((property) => ( 
          //para cada imóvel exibe um slide
            <SwiperSlide key={property.id}>
              <PropertyCard
              to={`/imovel/${property.id}`}
                key={property.id}
                title={property.nome}
                img={property.imagem || "https://plus.unsplash.com/premium_photo-1687960117069-567a456fe5f3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"} // Imagem padrão se não houver
                description={property.aminidades}
                price={property.preco}
              />
            </SwiperSlide>
          ))}
        </Swiper>
      </Slider>
      <Footer>
        <div className="footer-content">
          <h3>Entre em contato</h3>
          <p>E-mail: g4Construtora@gmail.com</p>
          <p>Telefone: (98) 99996666</p>
        </div>
      </Footer>
    </Container>
  )
}
