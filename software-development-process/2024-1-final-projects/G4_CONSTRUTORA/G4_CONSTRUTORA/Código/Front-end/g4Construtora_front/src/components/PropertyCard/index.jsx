import {Container, Image, AboutProperty} from "./styles"

export function PropertyCard({to,img,price,title,description}){
//   Este componente representa um cartão que exibe informações sobre um imóvel.
//  * Ele inclui uma imagem, título, descrição e preço do imóvel.
  return(
    <Container to = {to}>
     <Image src={img} alt={title} />
     <AboutProperty>
        <h1>{title}</h1>
        <p>{description}</p>
        <span>{price} R$</span>
      
     </AboutProperty>
    </Container>
  )
}