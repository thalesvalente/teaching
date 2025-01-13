import { Container } from "./styles";

export function Label ({htlmFor,children, ...rest}){
  return(
    <Container {...rest}>
      <label htmlFor= {htlmFor}>
        {children}
      </label>
    </Container>
  )
}
