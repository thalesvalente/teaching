import { Container } from "./styles";

export function Input({icon : Icon, width,...rest}){

  return(
    <Container width = {width}>  {/* Define o contêiner com a largura passada como prop */}
      {Icon && <Icon size = {20} />}  {/* Renderiza o ícone se ele for passado como prop */}
      <input {...rest}/>  {/* Espalha as outras props no elemento input */}
  
    </Container>

  )
}
