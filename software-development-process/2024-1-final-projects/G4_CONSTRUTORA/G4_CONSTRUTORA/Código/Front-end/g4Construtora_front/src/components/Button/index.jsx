import { Container } from "./styles";
//criam um componente botão
export function Button({title, label, ...rest}) {
 return (
  <Container type = "button" {...rest}> {/*recebe todas as propriedades adicionais (rest) que podem incluir eventos e outros atributos HTML*/}
    {title} {/*titulo do botão*/}
  </Container>
 ) 
}